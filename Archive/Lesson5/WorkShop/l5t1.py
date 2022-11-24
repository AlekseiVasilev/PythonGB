# 1. Создайте список из N натуральных чисел(0 до N),
# упорядоченных по возрастанию. Среди чисел не хватает
# одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
# Найдите это число

from secrets import choice


def create_list(len):
    temp_list = [i for i in range(len + 1)]
    temp_list.remove(choice(temp_list))
    return temp_list


def find_number(ls):
    for i in range(len(ls) // 2):
        if (ls[i] + 1 != ls[i + 1]):
            return ls[i] + 1
        elif (ls[-1 - i] - 1 != ls[-2 - i]):
            return ls[-1 - i] - 1
    return -1


new_list = create_list(int(input("Enter the value for list length: ")))
print(new_list)
print(find_number(new_list))
