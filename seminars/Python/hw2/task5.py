# 5. Реализуйте алгоритм перемешивания списка.

import random

list = [7, 2.25, -37037, 441.5, 0, 8319.94, 52]
list.sort()
print(list)

list.reverse()
print(list)

random.shuffle(list)
print(list)
