import numpy as np


class Route:
    def __init__(self):
        self.citys = []  # 所有地点和编号的对应关系
        self.simple_road = []  # 只包含指定目的地的编号
        self.entire_road = []  # 包含中间地点的编号
        self.min_distance = 1e9  # 最短路线长度
        self.signle_distance = []  # 每个目的地距离出发的距离
        self.simple_citys_name = []  # 目的地名称
        self.entire_citys_name = []  # 包含中间地点的名称

        with open("../address/citys_name.txt") as f:
            text = f.read().split('\n')
            for item in text:
                city = item.split(' ')
                self.citys.append(city)
        f.close()

    def Clear(self):
        self.simple_road = []
        self.entire_road = []
        self.min_distance = 1e9
        self.signle_distance = []

    def PrintInfo(self):
        print("简单路径：", self.simple_road)
        print("完整路径：", self.entire_road)
        print("最短距离：", self.min_distance)
        print("简单路径的地名：", self.simple_citys_name)
        print("完整路径的地名：", self.entire_citys_name)
        print("每个地点距离出发点距离：", self.signle_distance)


if __name__ == '__main__':
    r = Route()
    r.simple_road = [4, 7, 9, 11]
    r.entire_road = [1, 2, 3, 4]
    print(r.citys)
