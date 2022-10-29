import signal

import numpy as np
from Route import *


class TSP_BackTrack:
    road = Route()
    mat = []  # 邻接矩阵
    mat_floyd = []  # 弗洛伊德矩阵
    mat_pre = []  # 弗洛伊德前驱结点

    def __init__(self):
        self.read_txt()

    def read_txt(self):
        with open('../address/adj_mat.txt') as f_mat:
            entired_text = f_mat.read()
            for row in entired_text.split('\n'):
                for item in row.rstrip().split(' '):
                    self.mat.append(float(item))
            self.mat = np.array(self.mat).reshape((47, 47))

        with open('../address/adj_floyd_mat.txt') as floyd_mat:
            entired_text = floyd_mat.read()
            for row in entired_text.split('\n'):
                for item in row.rstrip().split(' '):
                    self.mat_floyd.append(float(item))
            self.mat_floyd = np.array(self.mat_floyd).reshape((47, 47))

        with open('../address/pre_mat.txt') as pre_mat:
            entired_text = pre_mat.read()
            for row in entired_text.split('\n'):
                for item in row.rstrip().split(' '):
                    self.mat_pre.append(int(item))
            self.mat_pre = np.array(self.mat_pre).reshape((47, 47))

    def ClearAll(self):
        self.road.clear()

    def backtrack(self, path, come, sum, used):
        if len(path) == len(self.pos):
            sum += self.mat_floyd[come][self.pos[0]]
            if sum < self.road.min_distance:
                self.road.min_distance = sum
                self.road.simple_road = path.copy()
                self.road.simple_road.append(self.pos[0])
            return
        for i in range(len(self.pos)):
            if used[i]:
                continue
            path.append(self.pos[i])
            used[i] = 1
            self.backtrack(path, self.pos[i], sum + self.mat_floyd[come][self.pos[i]], used)
            used[i] = 0
            path.pop()

    def get_entire_path(self):
        en_road = []
        pre_point = -1

        for item in self.road.simple_road:
            if pre_point != -1:
                self.get_two_point_road(pre_point, item)
            pre_point = item
            self.road.entire_road.append(item)

    def get_two_point_road(self, i, j):
        if j != self.mat_pre[i][j]:
            j = self.mat_pre[i][j]
            self.get_two_point_road(i, j)
            self.road.entire_road.append(j)

    def run(self, nums):
        self.pos = nums.copy()

        path = [self.pos[0]]
        used = np.zeros((len(self.pos),), dtype=int)
        used[0] = 1
        self.backtrack(path, self.pos[0], 0, used)
        self.get_entire_path()

        sum = 0
        for i in range(len(self.road.simple_road)-1):
            if i == 0:
                self.road.signle_distance.append(self.road.min_distance)
                continue

            city1 = self.road.simple_road[i - 1]
            city2 = self.road.simple_road[i]

            dis = self.mat_floyd[city1][city2]
            sum += dis
            self.road.signle_distance.append(sum)

        return self.road


if __name__ == '__main__':
    t = TSP_BackTrack()
    t.run([17, 22, 41, 33])
    print(t.road.simple_road)
    print(t.road.entire_road)
    print(t.road.min_distance)
    print(t.road.signle_distance)

