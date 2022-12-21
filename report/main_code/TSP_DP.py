import numpy as np
from TSP import TSP


class TSP_DP(TSP):
    def __init__(self, nums):
        super(TSP_DP, self).__init__()
        self.X = self.mat_floyd  # 距离矩阵
        self.result = []
        self.start_node = -1
        self.memory = {}
        self.nums = nums

    def run(self):
        self.start_node = self.nums[0]
        self.len = len(self.nums)
        self.used = [0 for i in range(self.len)]
        self.used[0] = 1
        self.result.append(self.start_node)
        node = self.start_node  # 初始节点
        self.road.min_distance = self.solve(node, self.used)  # 求解函数

        res = []
        for i in self.result:
            if i not in res:
                res.append(i)
        res.append(self.nums[0])
        self.road.simple_road = res
        self.GetEntireRoad()
        self.GetSignalDistance()
        self.GetCitysName()
        return self.road

    def solve(self, node, used):
        if sum(used) == self.len:
            return self.X[node][self.start_node]
        distance = []
        # 遍历未经历的节点
        for i in range(len(self.nums)):
            if used[i] == 1:
                continue
            node_j = self.nums[i]
            usedd = used.copy()
            usedd[i] = 1
            if self.memory.get(f"({node_j},{usedd})") is not None:
                distance.append([self.X[node][node_j] + self.memory[f"({node_j},{usedd})"], node_j])
            else:
                distance.append([self.X[node][node_j] + self.solve(node_j, usedd), node_j])
        d = np.min(distance, axis=0)[0]
        nodee = np.argmin(np.array(distance), axis=0)[0]
        next_one = distance[nodee][1]
        self.result.append(next_one)
        self.memory[f"({node},{used})"] = d
        return d


if __name__ == '__main__':
    t = TSP_DP([17, 22, 41, 33, 12, 19])
    road = t.run()
    road.PrintInfo()
