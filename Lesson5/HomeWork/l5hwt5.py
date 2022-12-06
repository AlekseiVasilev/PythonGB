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


def polynom_create(pow_val: int, file_name: str) -> None:
    """
    Creates polynom and writes it to the data.txt

    :param pow_val: [int] the highest pow in polynom
    :return: info to console
    """

    with open(f'{file_name}', 'a', encoding='UTF8') as file:
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
        print(f'Success!\nPolynom was wrote to the {file_name}!')


def polynom_concat(file_name_1: str, file_name_2: str):
    with open(f'{file_name_1}', 'r', encoding='UTF8') as file1:
        with open(f'{file_name_2}', 'r', encoding='UTF8') as file2:
            data1 = file1.readlines()
            data2 = file2.readlines()
            for i in data1:
                res1 = i.split()
                res1 = [(int(res1[k]), res1[k + 2]) for k in range(0, len(res1) - 2, 4)]
            for j in data2:
                res2 = j.split()
                res2 = [(int(res2[k]), res2[k + 2]) for k in range(0, len(res2) - 2, 4)]
            print(res1, res2)
            res_final = []
            if len(res1) >= len(res2):
                for i in range(len(res1)):
                    flag = True
                    for k in range(len(res2)):
                        if res2[k][1] == res1[i][1]:
                            res_final.append((res1[i][0]+res2[k][0], res1[i][1]))
                            flag = False
                            break
                    if flag:
                        res_final.append(res1[i])
                for i in range(len(res2)):
                    flag = True
                    for k in range(len(res1)):
                        if res1[k][1] == res2[i][1]:
                            flag = False
                            break
                    if flag:
                        res_final.append(res2[i])
                res_final = sorted(res_final, key=lambda x: x[1], reverse=True)






polynom_concat('data1.txt', 'data2.txt')
