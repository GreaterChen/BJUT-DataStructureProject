# -*- coding: utf-8 -*-
import random
import math
import time
import numpy as np

from geopy.distance import geodesic

SCORE_NONE = -1


def main():
    start = time.time()
    pos = [18, 23, 22, 41, 32]
    tsp = TSP_GA(pos)
    tsp.run(30)
    end = time.time()
    print(end - start, 's')


class TSP_GA(object):
    def __init__(self, selected_pos):
        # 格式为((经度,纬度),城市名,城市编号)
        self.citys = []
        self.selected_pos = selected_pos
        self.best_distance = -1
        self.simple_road = []
        self.entire_road = []
        self.floyd_mat = []
        self.pre_mat = []
        self.initCitys()
        self.individual_road = []
        self.ga = GA(aCrossRate=0.7,
                     aMutationRate=0.02,
                     aLifeCount=30,  # 种群规模
                     aGeneLength=len(self.selected_pos),  # 城市数量
                     aSelected_pos=self.selected_pos,  # 用户选中的城市数
                     aMatchFun=self.matchFun()
                     )

    def initCitys(self):
        with open('../address/address.txt', encoding='utf-8') as file:
            lines = file.readlines()

        for line in lines:
            building = line.strip('\n').split(' ')
            num = int(building[0])
            name = building[1]
            positions = building[2].split(',')
            pos_1 = float(positions[0])
            pos_2 = float(positions[1])
            self.citys.append((float(pos_2), float(pos_1), name, num))

        with open('../address/adj_floyd_mat.txt') as floyd_mat:
            entired_text = floyd_mat.read()
            for row in entired_text.split('\n'):
                for item in row.rstrip().split(' '):
                    self.floyd_mat.append(float(item))
            self.floyd_mat = np.array(self.floyd_mat).reshape((47, 47))

        with open('../address/pre_mat.txt') as pre_mat:
            entired_text = pre_mat.read()
            for row in entired_text.split('\n'):
                for item in row.rstrip().split(' '):
                    self.pre_mat.append(int(item))
            self.pre_mat = np.array(self.pre_mat).reshape((47, 47))

    def distance(self, road):
        distance = 0.0
        order = []
        # i从-1到32,-1是倒数第一个
        self.individual_road.clear()
        for i in range(-1, len(road) - 1):
            city1 = road[i]
            city2 = road[i + 1]
            order.append(city1)
            self.get_two_point_road(city1, city2, 1)
            order = self.individual_road

        for i in range(-1, len(order) - 1):
            index1, index2 = order[i], order[i + 1]
            city1, city2 = self.citys[index1], self.citys[index2]
            distance += geodesic((city1[1], city1[0]), (city2[1], city2[0])).m
        return distance

    # 适应度函数，因为我们要从种群中挑选距离最短的，作为最优解，所以（1/距离）最长的就是我们要求的
    def matchFun(self):
        return lambda life: 1.0 * 1000 / self.distance(life.gene)

    def run(self, n=100):
        while n > 0:
            self.ga.next()
            self.best_distance = self.distance(self.ga.best.gene)
            n -= 1
        return self.get_simple_road(), self.get_entire_road(), self.best_distance

    def get_simple_road(self):
        # print("经过%d次迭代，最优解距离为：%f" % (self.ga.generation, self.best_distance))
        # print("遍历城市顺序为：", )
        for i in self.ga.best.gene:
            self.simple_road.append(self.citys[i][3])
        return self.simple_road

    def get_entire_road(self):
        for i in range(-1, len(self.simple_road) - 1):
            city1 = self.simple_road[i]
            city2 = self.simple_road[i + 1]
            self.entire_road.append(city1)
            self.get_two_point_road(city1, city2)

        return self.entire_road

    def get_two_point_road(self, i, j, model=0):
        if model == 0:
            if j != self.pre_mat[i][j]:
                j = self.pre_mat[i][j]
                self.get_two_point_road(i, j)
                self.entire_road.append(j)
        elif model == 1:
            if j != self.pre_mat[i][j]:
                j = self.pre_mat[i][j]
                self.get_two_point_road(i,j,1)
                self.individual_road.append(j)


class Life(object):
    """个体类"""

    def __init__(self, aGene=None):
        self.gene = aGene
        self.score = SCORE_NONE


class GA(object):
    """遗传算法类"""

    def __init__(self, aCrossRate, aMutationRate, aLifeCount, aGeneLength, aSelected_pos, aMatchFun=lambda life: 1, ):
        self.crossRate = aCrossRate  # 交叉概率
        self.mutationRate = aMutationRate  # 突变概率
        self.lifeCount = aLifeCount  # 种群数量，就是每次我们在多少个城市序列里筛选，这里初始化为100
        self.geneLength = aGeneLength  # 其实就是城市数量
        self.matchFun = aMatchFun  # 适配函数
        self.lives = []  # 种群
        self.best = None  # 保存这一代中最好的个体
        self.generation = 1  # 一开始的是第一代
        self.crossCount = 0  # 一开始还没交叉过，所以交叉次数是0
        self.mutationCount = 0  # 一开始还没变异过，所以变异次数是0
        self.bounds = 0.0  # 适配值之和，用于选择时计算概率
        self.selected_pos = aSelected_pos

        self.initPopulation()  # 初始化种群

    def initPopulation(self):
        """初始化种群"""
        self.lives = []
        for i in range(self.lifeCount):
            gene = self.selected_pos.copy()
            random.shuffle(gene)
            life = Life(gene)
            self.lives.append(life)

    def judge(self):
        """评估，计算每一个个体的适配值"""
        # 适配值之和，用于选择时计算概率
        self.bounds = 0.0
        # 假设种群中的第一个基因被选中
        self.best = self.lives[0]
        for life in self.lives:
            life.score = self.matchFun(life)
            self.bounds += life.score
            # 如果新基因的适配值大于原先的best基因，就更新best基因
            if self.best.score < life.score:
                self.best = life

    def cross(self, parent1, parent2):
        """交叉"""
        index1 = random.randint(0, self.geneLength - 1)
        index2 = random.randint(index1, self.geneLength - 1)
        tempGene = parent2.gene[index1:index2]  # 交叉的基因片段
        newGene = []
        p1len = 0
        for g in parent1.gene:
            if p1len == index1:
                newGene.extend(tempGene)  # 插入基因片段
                p1len += 1
            if g not in tempGene:
                newGene.append(g)
                p1len += 1
        self.crossCount += 1
        return newGene

    def mutation(self, gene):
        """突变"""
        # 相当于取得0到self.geneLength - 1之间的一个数，包括0和self.geneLength - 1
        index1 = random.randint(0, self.geneLength - 1)
        index2 = random.randint(0, self.geneLength - 1)
        # 把这两个位置的城市互换
        gene[index1], gene[index2] = gene[index2], gene[index1]
        # 突变次数加1
        self.mutationCount += 1
        return gene

    def getOne(self):
        """选择一个个体"""
        # 产生0到（适配值之和）之间的任何一个实数
        # r = random.uniform(0, self.bounds)
        # for life in self.lives:
        #     r -= life.score
        #     if r <= 0:
        #         return life
        #
        # raise Exception("选择错误", self.bounds)
        r = random.randint(0, len(self.lives) - 1)
        return self.lives[r]

    def newChild(self):
        """产生新后的"""
        parent1 = self.getOne()
        rate = random.random()

        # 按概率交叉
        if rate < self.crossRate:
            # 交叉
            parent2 = self.getOne()
            gene = self.cross(parent1, parent2)
        else:
            gene = parent1.gene

        # 按概率突变
        rate = random.random()
        if rate < self.mutationRate:
            gene = self.mutation(gene)

        return Life(gene)

    def next(self):
        """产生下一代"""
        self.judge()  # 评估，计算每一个个体的适配值
        newLives = [self.best]
        while len(newLives) < self.lifeCount:
            newLives.append(self.newChild())
        self.lives = newLives
        self.generation += 1


if __name__ == '__main__':
    main()
