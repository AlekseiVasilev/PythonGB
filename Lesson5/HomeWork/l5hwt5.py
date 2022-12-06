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
from random import randint
from typing import List
from os import path


def polynom_create(pow_val: int, file_name: str) -> None:
    """
    Creates polynom and writes it to the data.txt

    :param file_name: uhmm...file name
    :param pow_val: [int] the highest pow in polynom
    :return: info to console
    """

    with open(f'{file_name}', 'w', encoding='UTF8') as file:
        coeff = random_list(pow_val + 1)
        if coeff[0] == 0:
            coeff[0] = randint(1, 100)
        result = ''
        for i in range(len(coeff) - 1):
            if coeff[i] != 0 and pow_val - i != 1:
                result += f'{coeff[i]} * x**{pow_val - i}'
                result += f' + '
            elif coeff[i] != 0 and pow_val - i == 1:
                result += f'{coeff[i]} * x'
                result += f' + '
        if coeff[-1] != 0:
            result += f'{coeff[-1]} = 0'
        else:
            result = result[:-2] + "= 0"
        file.write(f'{result}\n')
        print(f'Success!\nPolynom was wrote to the {file_name}!')


def readline_parser(file_name) -> List[tuple[int, str]]:
    """
    Takes input line and turn it to list with integer coefficient and x's pow tuple

    :param file_name: input file name
    :return: list with coefficient and x's pow tuple
    """

    data = file_name.readlines()
    res = None
    for i in data:
        res = i.split()
        res = [(int(res[k]), res[k + 2]) for k in range(0, len(res) - 2, 4)]
    return res


def find_same_tuple(data1: List[tuple[int, str]],
                    data2: List[tuple[int, str]]) -> List[tuple[int, str]]:
    """
    Searching for same x-pow in each of the lists and concatenate theirs coefficients

    :param data1: parsed line from first file
    :param data2: parsed line from second file
    :return: list with concatenated coefficients and x's pow tuple
    """

    data_final = []
    for i in range(len(data1)):
        flag = True
        for k in range(len(data2)):
            if data2[k][1] == data1[i][1]:
                data_final.append((data1[i][0] + data2[k][0], data1[i][1]))
                flag = False
                break
        if flag:
            data_final.append(data1[i])
    for i in range(len(data2)):
        flag = True
        for k in range(len(data1)):
            if data1[k][1] == data2[i][1]:
                flag = False
                break
        if flag:
            data_final.append(data2[i])
    data_final = sorted(data_final, key=lambda x: x[1], reverse=True)
    return data_final


def polynom_concat(file_name_1: str, file_name_2: str):
    """
    Full operation, that uses previous methods to get result string
    and write it to the file.

    :param file_name_1: input file 1
    :param file_name_2: input file 2
    :return: info to console
    """

    with open(f'{file_name_1}', 'r', encoding='UTF8') as file1:
        with open(f'{file_name_2}', 'r', encoding='UTF8') as file2:
            res1 = readline_parser(file1)
            res2 = readline_parser(file2)
            res_final = find_same_tuple(res1, res2)
    with open(f'poly_res.txt', 'w', encoding='UTF8') as file3:
        string_final = ''
        for i in range(len(res_final)):
            if res_final[i][1] != '0':
                string_final += f'{res_final[i][0]} * {res_final[i][1]} + '
            else:
                string_final += f'{res_final[i][0]} = {res_final[i][1]}\n'
        file3.write(string_final)
        return print('Success!\nResult polynom have been created at poly_res.txt\n')


def create_poly_option() -> None:
    """
    Calls methods to create polynom and put it to files

    :return: info to console
    """

    pow_input = give_int('Type the highest pow in first polynom: ', 1)
    polynom_create(pow_input, 'data1.txt')
    pow_input = give_int('Type the highest pow in second polynom: ', 1)
    polynom_create(pow_input, 'data2.txt')
    return print(f'Success!\nBoth polynom was wrote into files.\n')


def logic_menu(file_name1: str, file_name2: str, func) -> None:
    """
    Repeated code, that checks file for exist and starts method from parameter.

    :param file_name2: file name from outer operations
    :param file_name1: file name from outer operations
    :param func: method, that we want to call
    :return: info to console
    """

    if path.exists(fr'.\{file_name1}') and path.exists(fr'.\{file_name2}'):
        func(f'{file_name1}', f'{file_name2}')
    else:
        print(f'Files {file_name1} and {file_name2} are not exist in this folder.')
        print("Would you like to create them and put polynom in it? (Y/N)")
        if input().lower() in ('y', 'ye', 'yes'):
            create_poly_option()
        else:
            print(f"Create files {file_name1} and {file_name2} and put them to root folder\n")


def menu_input() -> None:
    """
    Creates console menu for user

    :return: info to console
    """

    while True:
        print('Type "1" if you want to create new polynom')
        print('Type "2" if you want to create result polynom')
        print('Type "-1" if you want to exit')
        num = input('What operation do you want to do?: ')
        if num == '1':
            create_poly_option()
        elif num == '2':
            logic_menu('data1.txt', 'data2.txt', polynom_concat)
        elif num == '-1':
            return exit(print("Bye-bye"))
        else:
            print("Incorrect value, try again!")


menu_input()
