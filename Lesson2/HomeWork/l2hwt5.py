# 5. ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

import random

start_list = list(range(0, 10))
print(start_list)
for i in range(0, len(start_list) - 1):
    temp_val = start_list[i]
    new_index = random.randint(0, len(start_list) - 1)
    start_list[i] = start_list[new_index]
    start_list[new_index] = temp_val
print(start_list)
