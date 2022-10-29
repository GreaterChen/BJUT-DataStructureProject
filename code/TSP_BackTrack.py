import numpy as np


class TSP_BackTrack:
    cost = 1e9  # 总路长
    pos = []  # 存储若干目的地
    res = []

    simple_road = []
    entire_road = []
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
        self.cost = 1e9
        self.pos.clear()
        self.res.clear()
        self.simple_road.clear()
        self.entire_road.clear()

    def backtrack(self, path, come, sum, used):
        if len(path) == len(self.pos):
            sum += self.mat_floyd[come][self.pos[0]]
            if sum < self.cost:
                self.cost = sum
                self.res.clear()
                self.res.append(path.copy())
            elif sum == self.cost:
                self.res.append(path.copy())
            return
        for i in range(len(self.pos)):
            if used[i]:
                continue
            path.append(self.pos[i])
            used[i] = 1
            self.backtrack(path, self.pos[i], sum + self.mat_floyd[come][self.pos[i]], used)
            used[i] = 0
            path.pop()

    def print_simple_path(self):
        return_simple_road = []
        simple_road = []

        for item in self.res[0]:
            simple_road.append(item)
            # print(item, '->', end=' ')
        # print(self.pos[0])
        simple_road.append(self.pos[0])
        return_simple_road.append(simple_road)
        return return_simple_road

    def print_entire_path(self):
        return_entire_road = []
        en_road = []
        pre_point = -1

        for item in self.res[0]:
            if pre_point != -1:
                self.entire_road.clear()
                self.get_two_point_road(pre_point, item)
                for i in self.entire_road:
                    en_road.append(i)
                    # print(i, '->', end=' ')
            pre_point = item
            en_road.append(item)
            # print(item, '->', end=' ')
        self.entire_road.clear()
        self.get_two_point_road(pre_point, self.pos[0])
        for i in self.entire_road:
            en_road.append(i)
            # print(i, '->', end=' ')
        en_road.append(self.pos[0])
        # print(self.pos[0])
        return_entire_road.append(en_road)
        return return_entire_road

    def get_two_point_road(self, i, j):
        if j != self.mat_pre[i][j]:
            j = self.mat_pre[i][j]
            self.get_two_point_road(i, j)
            self.entire_road.append(j)

    def tsp(self, nums):
        self.pos = nums.copy()

        path = [self.pos[0]]
        used = np.zeros((len(self.pos),), dtype=int)
        used[0] = 1
        self.backtrack(path, self.pos[0], 0, used)
        # print('总路程:', self.cost, 'm')
        self.simple_road = self.print_simple_path()
        self.entire_road = self.print_entire_path()

        return self.simple_road[0], self.entire_road[0], self.cost


if __name__ == '__main__':
    t = TSP_BackTrack()
    s, e, _ = t.tsp([3, 21, 39, 41, 34, 32, 18, 17, 16])
    print(s)
    print(e)
