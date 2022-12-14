from Route import *
import numpy as np


class TSP:
    def __init__(self):
        self.road = Route()
        self.mat = np.array([])
        self.mat_floyd = np.array([])
        self.mat_pre = np.array([], dtype=int)
        self.Readtxt()

    def Readtxt(self):
        with open('../address/adj_mat.txt') as f_mat:
            entired_text = f_mat.read()
            for row in entired_text.split('\n'):
                for item in row.rstrip().split(' '):
                    self.mat = np.append(self.mat, float(item))
        self.mat = self.mat.reshape((47, 47))

        with open('../address/adj_floyd_mat.txt') as floyd_mat:
            entired_text = floyd_mat.read()
            for row in entired_text.split('\n'):
                for item in row.rstrip().split(' '):
                    self.mat_floyd = np.append(self.mat_floyd, float(item))
        self.mat_floyd = self.mat_floyd.reshape((47, 47))

        with open('../address/pre_mat.txt') as pre_mat:
            entired_text = pre_mat.read()
            for row in entired_text.split('\n'):
                for item in row.rstrip().split(' '):
                    self.mat_pre = np.append(self.mat_pre, int(item))
        self.mat_pre = self.mat_pre.reshape((47, 47))

    def ClearAll(self):
        self.road.Clear()

    def GetMinDistance(self):
        sum = 0.0
        road = self.road.simple_road[:-1]
        for item in range(len(road)):
            city1 = road[item - 1]
            city2 = road[item]
            dis = self.mat_floyd[city1][city2]
            sum += dis
        self.road.min_distance = sum

    def GetEntireRoad(self):
        pre_point = -1
        for item in self.road.simple_road:
            if pre_point != -1:
                self.GetTwoPointRoad(pre_point, item)
            pre_point = item
            self.road.entire_road.append(item)

    def GetTwoPointRoad(self, i, j):
        if j != self.mat_pre[i][j]:
            j = self.mat_pre[i][j]
            self.GetTwoPointRoad(i, j)
            self.road.entire_road.append(j)

    def GetSignalDistance(self):
        sum = 0
        for i in range(len(self.road.simple_road) - 1):
            if i == 0:
                self.road.signle_distance.append(self.road.min_distance)
                continue

            city1 = self.road.simple_road[i - 1]
            city2 = self.road.simple_road[i]

            dis = self.mat_floyd[city1][city2]
            sum += dis
            self.road.signle_distance.append(sum)

    def GetCitysName(self):
        self.road.simple_citys_name.clear()
        self.road.entire_citys_name.clear()

        for item in self.road.simple_road:
            self.road.simple_citys_name.append(self.road.citys[item][1])
        # self.simple_citys_name.pop()

        for item in self.road.entire_road:
            self.road.entire_citys_name.append(self.road.citys[item][1])
        # self.entire_citys_name.pop()
