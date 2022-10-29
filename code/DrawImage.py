import cv2
import numpy as np
from Route import *


class DrawRoad:
    x_base = 226
    y_base = 58
    x = []
    y = []

    def __init__(self, add):
        self.add = add + '/res.jpg'
        print(self.add)
        self.img = cv2.imread('../images/school_map.jpg')
        self.ReadAxis()

    def ChangeAdd(self, add):
        self.add = add

    def ReadAxis(self):
        with open('../address/axis_x.txt') as f:
            text = f.read().split(' ')
            for item in text:
                self.x.append(int(item))

        with open('../address/axis_y.txt') as f:
            text = f.read().split(' ')
            for item in text:
                self.y.append(int(item))

    def axis_change(self, x, y):
        return x - self.x_base, y - self.y_base

    def DrawImage(self, road: Route):
        print(road.entire_road)
        print(road.simple_road)
        pos = road.entire_road.copy()
        simple_pos = road.simple_road.copy()
        for i in range(len(pos) - 1):
            x1, y1 = self.axis_change(self.x[pos[i]], self.y[pos[i]])
            x2, y2 = self.axis_change(self.x[pos[i + 1]], self.y[pos[i + 1]])
            if pos[i] in simple_pos:
                cv2.circle(self.img, (x1, y1), 1, (193, 59, 0), 20)
            else:
                cv2.circle(self.img, (x1, y1), 1, (167, 131, 65), 15)
            cv2.line(self.img, (x1, y1), (x2, y2), (96, 110, 196), 5, lineType=cv2.LINE_AA)  # plot line
        cv2.imencode('.jpg', self.img)[1].tofile(self.add)
        cv2.imwrite('../images/school_map_change.jpg', self.img)  # 保存图片

    def DrawImage_order(self, entired_res, simple_res):
        pos = entired_res
        simple_pos = simple_res
        simple_pos.append(simple_pos[0])
        for i in range(len(pos) - 1):
            x1, y1 = self.axis_change(self.x[pos[i]], self.y[pos[i]])
            x2, y2 = self.axis_change(self.x[pos[i + 1]], self.y[pos[i + 1]])
            if pos[i] in simple_pos:
                cv2.circle(self.img, (x1, y1), 1, (193, 59, 0), 20)
            else:
                cv2.circle(self.img, (x1, y1), 1, (167, 131, 65), 15)
            cv2.line(self.img, (x1, y1), (x2, y2), (96, 110, 196), 5, lineType=cv2.LINE_AA)  # plot line
        cv2.imencode('.jpg', self.img)[1].tofile(self.add)
        cv2.imwrite('../images/school_map_change.jpg', self.img)  # 保存图片


if __name__ == '__main__':
    en = [5, 7, 16, 18, 20, 32, 33, 45, 44, 43, 41, 39, 36, 22, 11, 14, 13, 2, 3, 5]
    si = [5, 18, 33, 44, 41, 39, 36, 11, 5]
    d = DrawRoad()
    d.DrawImage(en, si)
    # cv2.imshow('image', img)
    # cv2.waitKey(0)  # 等待按键反应
    # cv2.destroyAllWindows()
    # DrawImage(en, si)
