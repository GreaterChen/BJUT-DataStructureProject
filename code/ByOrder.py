import numpy as np
from geopy.distance import geodesic


class ByOrder:
    def __init__(self, selected_pos):
        self.citys = []
        self.floyd_mat = []
        self.pre_mat = []
        self.simple_road = []
        self.entire_road = []
        self.selected_pos = selected_pos
        self.initCity()

    def initCity(self):
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

    def GetRoad(self):
        distance = 0.0

        self.simple_road = self.selected_pos

        for i in range(0, len(self.selected_pos) - 1):
            city1 = self.simple_road[i]
            city2 = self.simple_road[i + 1]
            self.entire_road.append(city1)
            self.get_two_point_road(city1, city2)

        self.entire_road.append(self.selected_pos[-1])

        for i in range(0, len(self.entire_road) - 1):
            index1, index2 = self.entire_road[i], self.entire_road[i + 1]
            city1, city2 = self.citys[index1], self.citys[index2]
            distance += geodesic((city1[1], city1[0]), (city2[1], city2[0])).m

        return self.simple_road, self.entire_road, distance

    def get_two_point_road(self, i, j):
        if j != self.pre_mat[i][j]:
            j = self.pre_mat[i][j]
            self.get_two_point_road(i, j)
            self.entire_road.append(j)


if __name__ == '__main__':
    pos = [33, 17, 21, 41]
    t = ByOrder(pos)
    q, w, e = t.GetRoad()
    print(q)
    print(w)
    print(e)
