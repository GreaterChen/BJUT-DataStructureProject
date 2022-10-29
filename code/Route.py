class Route:
    citys = []

    def __init__(self):
        self.simple_road = []
        self.entire_road = []
        self.min_distance = 1e9
        self.signle_distance = []
        self.simple_citys_name = []
        self.entire_citys_name = []

    def clear(self):
        self.simple_road = []
        self.entire_road = []
        self.min_distance = 1e9
        self.signle_distance = []

    def GetCitysName(self):
        self.simple_citys_name.clear()
        self.entire_citys_name.clear()
        with open("../address/citys_name.txt") as f:
            text = f.read().split('\n')
            for item in text:
                city = item.split(' ')
                self.citys.append(city)

        for item in self.simple_road:
            self.simple_citys_name.append(self.citys[item][1])
        self.simple_citys_name.pop()

        for item in self.entire_road:
            self.entire_citys_name.append(self.citys[item][1])
        self.entire_citys_name.pop()


if __name__ == '__main__':
    r = Route()
    r.simple_road = [4, 7, 9, 11]
    r.entire_road = [1, 2, 3, 4]
    r.GetCitysName()
    print(r.citys)
