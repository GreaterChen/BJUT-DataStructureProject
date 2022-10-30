import random

from PyQt5.QtCore import *

gen = [1, 4, 2, 6, 8]
gen2 = [1,4,2,6]

print(list(set(gen)-set(gen2)))