# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

from os import path
from itertools import groupby


def file_system() -> None:
    """
    Initializing file system for program, as we need file with start info,
    file with encrypted data, and file with deciphered data

    :return: info to console
    """

    with open("data.txt", "w", encoding="UTF-8"):
        with open("data_enc.txt", "w", encoding="UTF-8"):
            with open("data_dec.txt", "w", encoding="UTF-8"):
                return print('Success! File system initialized.\n'
                             'Files data.txt, data_enc.txt, data_dec.txt added to the root folder.')


def logic_menu(file_name: str, func) -> None:
    """
    Repeated code, that checks file for exist and starts method from parameter.

    :param file_name: file name from outer operations
    :param func: method, that we want to call
    :return: info to console
    """

    if path.exists(fr'.\{file_name}'):
        func()
    else:
        print(f'File {file_name} is not exist in this folder.')
        print("Would you like to initialize file system? (Y/N)")
        if input().lower() in ('y', 'ye', 'yes'):
            file_system()
        else:
            print(f"Create file {file_name} and put it to root folder\n")


def menu_input() -> None:
    """
    Creates console menu for user

    :return: info to console
    """

    while True:
        print('Type "1" if you want to initialize file system')
        print('Type "2" if you want to put some text to the start file')
        print('Type "3" if you want to create encrypted file')
        print('Type "4" if you want to decipher existing file')
        print('Type "-1" if you want to exit')
        num = input('What operation do you want to do?: ')
        if num == '1':
            file_system()
        elif num == '2':
            with open("data.txt", "w", encoding="UTF-8") as file:
                file.write(input('Type something:\n>> '))
        elif num == '3':
            logic_menu('data.txt', enc_rle)
        elif num == '4':
            logic_menu('data_enc.txt', dec_rle)
        elif num == '-1':
            return exit(print("Bye-bye"))
        else:
            print("Incorrect value, try again!")


def enc_rle() -> None:
    """
    Method that allows us encrypt data with RLE method. Counts repeating symbols
    and put result string to the file.

    :return: info to console
    """

    with open("data.txt", 'r', encoding="UTF-8") as no_code_rle:
        with open("data_enc.txt", 'w', encoding="UTF-8") as code_rle:
            nocode_data = list(no_code_rle.readline())
            result = []
            for i, j in groupby(nocode_data):
                result.append(str(len(list(j))))
                result.append(i)
                result_string = ''
            for i in result:
                if i != '1':
                    result_string += i
            code_rle.write(result_string)
    return print('Success!\nData was encrypted in data_enc.txt')


def dec_rle() -> None:
    """
    Method that allows us to decipher data with RLE method. Sorts out input string,
    multiplies amount of symbols with themselves, and put result string to the file.

    :return: info to console
    """

    with open("data_enc.txt", 'r', encoding="UTF-8") as code_rle:
        with open("data_dec.txt", 'w', encoding="UTF-8") as no_code_rle:
            code_data = code_rle.readline()
            temp_ls = ['']
            k = 0
            for i in range(len(code_data)):
                if code_data[i].isdigit():
                    temp_ls[k] += code_data[i]
                else:
                    temp_ls.append(code_data[i])
                    temp_ls.append('')
                    if temp_ls[k] == '':
                        temp_ls[k] = '1'
                    no_code_rle.write(f'{int(temp_ls[k]) * temp_ls[k + 1]}')
                    k += 2
    return print('Success!\nData was deciphered in data_dec.txt')


menu_input()
