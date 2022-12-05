# Задана натуральная степень n. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример:
# - n=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 (коэф: []) или 10*x² = 0
# Уточнения:
# n - это степень икса первого элемента полинома
# при n =3 => 5*x*3 + 18*x2 + 7*x + 19 = 0 - коэффициенты = [5,18,7,19]
# при n=2 => 2*x² + 4*x + 5 = 0(коэф: [2,4,5]) или x² + 5 = 0 (коэф: [1,0,5]) или 10*x²(коэф: [10,0,0]) = 0
# при n=10 => 56 * x*10 = 0
# коэффициенты - это числа перед элементами полинома.
# коэффициенты могут быть нулем, кроме первого

from gbfunctions import give_int, random_list
from random import choice, randint


def polynom_create(pow_val: int) -> None:
    """
    Creates polynom and writes it to the data.txt

    :param pow: [int] highest pow in polynom
    :return: info to console
    """
    with open('data.txt', 'a', encoding='UTF8') as file:
        coeff = random_list(pow_val + 1)
        if coeff[0] == 0:
            coeff[0] = randint(1, 100)
        result = ''
        for i in range(len(coeff) - 1):
            if coeff[i] != 0 and pow_val - i != 1:
                result += f'{coeff[i]} * x**{pow_val - i}'
                result += f' {choice("+-")} '
            elif coeff[i] != 0 and pow_val - i == 1:
                result += f'{coeff[i]} * x'
                result += f' {choice("+-")} '
        if coeff[-1] != 0:
            result += f'{coeff[-1]} = 0'
        else:
            result = result[:-2] + "= 0"
        file.write(f'{result}\n')
        print('Success!\nPolynom was wrote to the data.txt!')


pow_input = give_int('Type highest power in polynom:\n>> ', 1)
polynom_create(pow_input)
