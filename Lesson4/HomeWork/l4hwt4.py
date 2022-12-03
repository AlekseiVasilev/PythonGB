# 4- Шифр Цезаря - это способ шифрования,
# где каждая буква смещается на определенное количество символов влево или вправо.
# При расшифровке происходит обратная операция. Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст,
# а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.

from string import *
from os import path


def file_create() -> None:
    """
    Creates caesar_enc.txt file

    :return: info about operation
    """

    with open('caesar_enc.txt', 'w', encoding='UTF8') as file:
        input_string = input("Type any information you want:\n>> ")
        file.write(input_string)
    return print("Success!\nYou have created caesar_enc.txt\n")


def enc_key_caesar() -> int:
    """
    Asking encryption key from user, which calculated from input string to number.
    Key format: 1r - 25r; 1l - 25l
    Why 25? It's range of the biggest string, where we try to find our symbol (ascii_lowercase for ex.)
    If we try 0 or 26, then symbol will not change
    r - means right, or "+" operation; l - means left, or "-" operation

    :return: [int] encryption key
    """

    while True:
        enc_key = []
        key = input('Type key for caesar encryption.\n'
                    'For ex.: 2L - 2 symbols left, 3R - 3 symbols right\n'
                    '>> ').lower()
        enc_key.append(key[0])
        for i in range(1, len(key)):
            if key[i].isdigit():
                enc_key[0] += key[i]
            else:
                enc_key.append(key[i])
        try:
            if len(enc_key) > 2 or not enc_key[0].isdigit() or not enc_key[1] in ('r', 'l'):
                print('Key contains only natural number (from 1 to 25) and one letter (r, l). Try again!')
                continue
        except IndexError:
            print('Key contains only natural number (from 1 to 25) and one letter (r, l). Try again!')
            continue
        else:
            if 0 < int(enc_key[0]) < 26:
                break
            print('Type number from 1 to 25.')
            continue
    if enc_key[1] == 'r':
        enc_key[1] = 1
    elif enc_key[1] == 'l':
        enc_key[1] = -1
    enc_key = int(enc_key[0]) * int(enc_key[1])
    return enc_key


def logic_enc(line, i: int, key: int, func: str):
    """
    Repeated code, that we use in encryption method.

    :param line: List[str] from method
    :param i: iterator value from cycle in method
    :param key: encryption key from method
    :param func: string where we are trying to find symbol from input_string
    :return: line[i] value
    """

    symbol_index = func.find(line[i])
    if symbol_index >= 0:
        symbol_index = symbol_index + key
        if symbol_index > (len(func) - 1) or symbol_index < (len(func) - 1) * (-1):
            symbol_index = symbol_index % len(func)
        line[i] = func[symbol_index]
    return line[i]


def logic_dec(line, i: int, key: int, func: str):
    """
    Repeated code, that we use in decipher method. Yes, it's only replaces "+" by "-"
    Roman, could we unite this logic's methods by additional parameter?

    :param line: List[str] from method
    :param i: iterator value from cycle in method
    :param key: encryption key from method
    :param func: string where we are trying to find symbol from input_string
    :return:
    """

    symbol_index = func.find(line[i])
    if symbol_index >= 0:
        symbol_index = symbol_index - key
        if symbol_index > (len(func) - 1) or symbol_index < (len(func) - 1) * (-1):
            symbol_index = symbol_index % len(func)
        line[i] = func[symbol_index]
    return line[i]


def enc_func_caesar(key: int) -> None:
    """
    Encryption method, which takes encryption key and applies it to each symbol

    :param key: [int] encryption key
    :return: info to console
    """

    with open('caesar_enc.txt', 'r', encoding='UTF8') as file:
        line = list(file.readline())
        for i in range(len(line)):
            if line[i] in ascii_lowercase:
                line[i] = logic_enc(line, i, key, ascii_lowercase)
            elif line[i] in ascii_uppercase:
                line[i] = logic_enc(line, i, key, ascii_uppercase)
            elif line[i] in digits:
                line[i] = logic_enc(line, i, key, digits)
            elif line[i] in punctuation:
                line[i] = logic_enc(line, i, key, punctuation)
        enc_data = ''.join(line)
    with open('caesar_enc.txt', 'w', encoding='UTF8') as file:
        file.write(enc_data)
    return print('Success!\nInformation was encrypted in caesar_enc.txt')


def dec_func_caesar(key: int) -> None:
    """
    Decipher method, which takes encryption key and applies it to each symbol

    :param key: [int] encryption key
    :return: info to console
    """

    with open('caesar_enc.txt', 'r', encoding='UTF8') as file:
        line = list(file.readline())
        for i in range(len(line)):
            if line[i] in ascii_lowercase:
                line[i] = logic_dec(line, i, key, ascii_lowercase)
            elif line[i] in ascii_uppercase:
                line[i] = logic_dec(line, i, key, ascii_uppercase)
            elif line[i] in digits:
                line[i] = logic_dec(line, i, key, digits)
            elif line[i] in punctuation:
                line[i] = logic_dec(line, i, key, punctuation)
        enc_data = ''.join(line)
    with open('caesar_enc.txt', 'w', encoding='UTF8') as file:
        file.write(enc_data)
    return print('Success!\nInformation was deciphered in caesar_enc.txt')


def logic_menu(func) -> None:
    """
    Repeated code, that checks file for exist and starts method from parameter.

    :param func: method, that we want to call
    :return: None
    """

    if path.exists(fr'.\caesar_enc.txt'):
        caesar_key = enc_key_caesar()
        func(key=caesar_key)
    else:
        print('File caesar_enc.txt is not exist in this folder.')
        print("Would you like to create file? (Y/N)")
        if input().lower() in ('y', 'ye', 'yes'):
            file_create()
        else:
            print("Create file caesar_enc.txt and put it to root folder\n")


def menu_input():
    """
    Creates console menu for user

    :return:
    """

    while True:
        print('Type "1" if you want to create file')
        print('Type "2" if you want to create encrypted file')
        print('Type "3" if you want to decipher existing file')
        print('Type "-1" if you want to exit')
        num = input('What operation do you want to do?: ')
        if num == '1':
            file_create()
        elif num == '2':
            logic_menu(enc_func_caesar)
        elif num == '3':
            logic_menu(dec_func_caesar)
        elif num == '-1':
            return exit(print("Bye-bye"))
        else:
            print("Incorrect value, try again!")


menu_input()
