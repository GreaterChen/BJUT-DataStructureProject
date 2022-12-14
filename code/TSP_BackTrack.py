import signal

import numpy as np
from TSP import *


class TSP_BackTrack(TSP):
    def __init__(self):
        super(TSP_BackTrack, self).__init__()

    def run(self, nums):
        self.pos = nums.copy()
        path = [self.pos[0]]
        used = np.zeros((len(self.pos),), dtype=int)
        used[0] = 1
        self.backtrack(path, self.pos[0], 0, used)
        self.GetEntireRoad()
        self.GetSignalDistance()
        self.GetCitysName()
        return self.road

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


if __name__ == '__main__':
    t = TSP_BackTrack()
    road = t.run([17, 22, 41, 33])
    road.PrintInfo()
