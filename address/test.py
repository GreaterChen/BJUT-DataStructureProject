import numpy as np

with open('address.txt', encoding='utf-8') as file:
    lines = file.readlines()
print(lines)

buildings = []
adj_mat = np.zeros((47, 47))

for line in lines:
    building = line.strip('\n').split(' ')
    num = int(building[0])
    name = building[1]
    positions = building[2].split(',')
    pos_1 = float(positions[0])
    pos_2 = float(positions[1])
    buildings.append([num, name, pos_2, pos_1])

print(buildings)