# 1. Задайте строку из набора чисел. Напишите программу,
# которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

def check(str_list):
    for i, num in enumerate(str_list):
        str_list[i] = num.strip('.,;:?!')
        if not str_list[i].replace("-", "").isdigit():
            return []
    return str_list


def find_max_min(nums_str: str):
    list_nums = nums_str.split()
    right_list = check(list_nums)

    if right_list:
        return min(right_list, key=int), max(right_list, key=int)
    else:
        print("The data is incorrect")
        return []


print(*find_max_min(input("Enter the numbers separated by a space: ")))
