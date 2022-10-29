class Route:
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

    def GetCitysName(self,simple_road = self.simple_road,entire_road=self.entire_road):
        self.simple_citys_name.clear()
        self.entire_citys_name.clear()
        citys = []
        with open("../address/citys_name.txt") as f:
            text = f.read().split('\n')
            for item in text:
                city = item.split(' ')
                citys.append(city)

        for item in simple_road:
            self.simple_citys_name.append(citys[item][1])

        for item in entire_road:
            self.entire_citys_name.append(citys[item][i])

if __name__ == '__main__':
    r = Route()
    r.simple_road = [4,7,9,11]
    r.GetCitysName()
