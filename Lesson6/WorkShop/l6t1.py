# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.


def priority(data, arg1, arg2):
    for i in range(len(data)):
        try:
            ind1 = data.index(arg1)
        except ValueError:
            ind1 = -1
        try:
            ind2 = data.index(arg2)
        except ValueError:
            ind2 = -1
        min_ind = min(ind1, ind2)
        max_ind = max(ind1, ind2)
        if min_ind != -1:
            data[min_ind - 1] = op(data[min_ind], data[min_ind - 1], data[min_ind + 1])
            data.pop(min_ind)
            data.pop(min_ind)
        elif min_ind == -1 and max_ind != -1:
            data[max_ind - 1] = op(data[max_ind], data[max_ind - 1], data[max_ind + 1])
            data.pop(max_ind)
            data.pop(max_ind)
        elif min_ind == max_ind == -1:
            break
    return data


def op(oper: str, arg1: str, arg2: str):
    if oper == '*':
        return int(arg1) * int(arg2)
    elif oper == '/':
        return int(arg1) / int(arg2)
    elif oper == '+':
        return int(arg1) + int(arg2)
    elif oper == '-':
        return int(arg1) - int(arg2)


lst = input().split()
lst = priority(lst, '/', '*')
print(lst)
lst = priority(lst, '-', '+')
print(f'Result = {lst[0]}')
