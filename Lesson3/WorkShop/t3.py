# 3.Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def input_method():
    num = ""
    while not num.isdigit():
        num = input('Enter value: ')
        if num.isdigit():
            num = int(num)
            return num
        elif num == -1:
            exit('Bye-bye')
        else:
            print('Value is incorrect\nIf you want to exit the program then type "-1"')


def func_n(number):
    number = 3 * number + 1
    return number


length = input_method()
dict = {i: func_n(i) for i in range(length + 1)}
print(dict)
