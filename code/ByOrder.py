import numpy as np
from geopy.distance import geodesic
from TSP import *


class ByOrder(TSP):
    def __init__(self, selected_pos):
        super(ByOrder, self).__init__()
        self.selected_pos = selected_pos.copy()

    def run(self):
        self.road.simple_road = self.selected_pos
        self.road.simple_road.append(self.selected_pos[0])
        self.get_entire_path()
        self.get_min_distance()
        self.road.GetCitysName()
        self.GetSignalDistance()
        return self.road




