# 3. Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.


from gbfunctions import give_int, random_list_float


def max_min_fract(datalist: list) -> float:
    '''
    Gives difference between maximum fractal part and minimum fractal part of elements in list.
    Fractal part getting by reminder of division by 1.
    Magical number "4" is amount of digits after dot...Python zen!
    Remember one thing:
    -5.9 = -6 + 0.1   fract_part = 0.1 <- !!!That's math bro/sis!!!

    :param datalist: list with elements
    :return: difference between maximum fractal part and minimum
    '''

    max_fract = 0.0
    min_fract = 1.0
    for i in range(len(datalist)):
        fract_part = round(datalist[i] % 1, 4)
        if fract_part >= max_fract:
            max_fract = fract_part
        if fract_part <= min_fract:
            min_fract = fract_part
    print('Max fractal part:', max_fract)
    print('Max fractal part:', min_fract)
    summ = round(max_fract - min_fract, 4)
    return summ


size = give_int('Type value for length of the list: ', 1)
numbers = random_list_float(size)
print(numbers)   # -7 + 0.1068
print(f'Difference is: {max_min_fract(numbers)}')
