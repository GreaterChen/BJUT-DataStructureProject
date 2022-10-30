import random

from PyQt5.QtCore import *

gen = [1, 4, 2, 6, 8]
t = gen[1:]
random.shuffle(t)
print(t)
t.insert(0, gen[0])
print(t)