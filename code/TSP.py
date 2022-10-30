from Route import *
import numpy as np


class TSP:
    def __init__(self):
        self.road = Route()
        self.mat = np.array([])
        self.mat_floyd = np.array([])
        self.mat_pre = np.array([], dtype=int)
        self.read_txt()

    def read_txt(self):
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
        self.road.clear()

    def get_entire_path(self):
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
