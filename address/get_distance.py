from geopy.distance import geodesic
import numpy as np
from math import *
from pylab import *

with open('address.txt', encoding='utf-8') as file:
    lines = file.readlines()

buildings = []
adj_mat = np.zeros((47, 47))

for line in lines:
    building = line.strip('\n').split(' ')
    num = int(building[0])
    name = building[1]
    positions = building[2].split(',')
    pos_1 = float(positions[0])
    pos_2 = float(positions[1])
    buildings.append([num, name, pos_1, pos_2])

# 每个建筑的相邻建筑
neighbor = np.array([
    [1, 2],  # 0
    [0, 2, 8, 9],
    [0, 1, 3, 4, 9, 12],
    [2, 4, 5, 46],
    [2, 3, 6],
    [3, 46, 6, 7],
    [4, 5, 7],
    [5, 6, 16],
    [1, 10, 21],
    [1, 2, 10, 11, 12],  # 9

    [8, 9, 11, 21],  # 10
    [9, 10, 14, 21, 22],
    [2, 9, 13, 16],
    [12, 14, 15],
    [11, 13, 23],
    [13, 17, 23, 31],
    [7, 12, 17, 18, 19],
    [15, 16, 18, 20, 31],
    [16, 17, 19, 20],
    [16, 18],  # 19

    [17, 18, 32],  # 20
    [8, 10, 11, 22, 35, 36],
    [11, 21, 23, 24, 25, 26, 35, 36],
    [14, 15, 22, 24, 27, 31],
    [22, 23, 25],
    [22, 24, 26, 28, 29],
    [22, 25, 30, 36, 37],
    [23, 28, 31],
    [25, 27, 29, 31],
    [25, 28, 30, 31],  # 29

    [26, 29, 31, 37, 41],  # 30
    [15, 17, 23, 27, 28, 29, 30, 32, 34, 41, 42],
    [20, 31, 33, 34],
    [32, 34, 42, 45],
    [31, 32, 33, 42],
    [21, 22, 36, 40],
    [21, 22, 26, 35, 37, 38, 39, 40],
    [26, 30, 36, 38],
    [36, 37, 39, 41],
    [36, 38, 40, 41],  # 39

    [35, 36, 39],  # 40
    [30, 31, 38, 39, 42, 43],
    [31, 33, 34, 41, 43, 45],
    [41, 42, 44],
    [43, 45],
    [33, 42, 44],
    [3, 5]  # 46
])


def check_neighbor():
    for i in neighbor:
        for j in neighbor[i]:
            if i not in neighbor[j]:
                print(i, j)




# 获得邻接矩阵并写入文件
for i in range(47):
    for j in neighbor[i]:
        dis = geodesic((buildings[i][2], buildings[i][3]), (buildings[j][2], buildings[j][3])).m
        adj_mat[i][j] = dis

for i in range(47):
    for j in range(47):
        if adj_mat[i][j] == 0.0:
            adj_mat[i][j] = 1e7

with open("adj_mat.txt", 'w') as file:
    for i in range(47):
        for j in range(47):
            file.write(str(adj_mat[i][j]))
            file.write(' ')
        file.write('\n')

file.close()

# 使用Floyd算法计算两点间最短路径并写入文件
lengthD = len(adj_mat)  # 邻接矩阵大小
p = list(range(lengthD))
pre_mat = []
for i in range(lengthD):
    pre_mat.append(p)
pre_mat = array(pre_mat)

for i in range(lengthD):
    for j in range(lengthD):
        for k in range(lengthD):
            if adj_mat[i, j] > adj_mat[i, k] + adj_mat[j, k]:  # 两个顶点直接较小的间接路径替换较大的直接路径
                adj_mat[i, j] = adj_mat[i, k] + adj_mat[j, k]
                pre_mat[i, j] = pre_mat[j, k]  # 记录新路径的前驱
# print(pre_mat)
# print(adj_mat)


with open("pre_mat.txt", 'w') as file:
    for i in range(47):
        for j in range(47):
            file.write(str(pre_mat[i][j]))
            file.write(' ')
        file.write('\n')

file.close()

with open("adj_floyd_mat.txt", 'w') as file:
    for i in range(47):
        for j in range(47):
            file.write(str(adj_mat[i][j]))
            file.write(' ')
        file.write('\n')

file.close()

road = []


# 回溯得到最短路径
def get_road(i, j):
    if j != pre_mat[i][j]:
        j = pre_mat[i][j]
        get_road(i, j)
        road.append(j)


if __name__ == '__main__':
    print(neighbor[22])
