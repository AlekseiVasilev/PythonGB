# 4- Шифр Цезаря - это способ шифрования,
# где каждая буква смещается на определенное количество символов влево или вправо.
# При расшифровке происходит обратная операция. Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст,
# а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.

from string import *
from os import path


def file_create() -> None:
    '''
    Creates caesar_enc.txt file

    :return: info about operation
    '''

    with open('caesar_enc.txt', 'w', encoding='UTF8') as file:
        input_string = input("Type any information you wan't:\n>> ")
        file.write(input_string)
    return print("Success!\nYou have created caesar_enc.txt\n")


def enc_key_caesar() -> int:
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


def enc_func_caesar(key: int) -> None:
    with open('caesar_enc.txt', 'r', encoding='UTF8') as file:
        line = list(file.readline())
        for i in range(len(line)):
            if line[i] in ascii_lowercase:
                symbol_index = ascii_lowercase.find(line[i])
                if symbol_index >= 0:
                    symbol_index = symbol_index + key
                    if symbol_index > (len(ascii_lowercase) - 1) or symbol_index < (len(ascii_lowercase) - 1) * (-1):
                        symbol_index = symbol_index % len(ascii_lowercase)
                    line[i] = ascii_lowercase[symbol_index]
            elif line[i] in ascii_uppercase:
                symbol_index = ascii_uppercase.find(line[i])
                if symbol_index >= 0:
                    symbol_index = symbol_index + key
                    if symbol_index > (len(ascii_uppercase) - 1) or symbol_index < (len(ascii_uppercase) - 1) * (-1):
                        symbol_index = symbol_index % len(ascii_uppercase)
                    line[i] = ascii_uppercase[symbol_index]
            elif line[i] in digits:
                symbol_index = digits.find(line[i])
                if symbol_index >= 0:
                    symbol_index = symbol_index + key
                    if symbol_index > (len(digits) - 1) or symbol_index < (len(digits) - 1) * (-1):
                        symbol_index = symbol_index % len(digits)
                    line[i] = digits[symbol_index]
            elif line[i] in punctuation:
                symbol_index = punctuation.find(line[i])
                if symbol_index >= 0:
                    symbol_index = symbol_index + key
                    if symbol_index > (len(punctuation) - 1) or symbol_index < (len(punctuation) - 1) * (-1):
                        symbol_index = symbol_index % len(punctuation)
                    line[i] = punctuation[symbol_index]
        enc_data = ''.join(line)
        print(enc_data)
    with open('caesar_enc.txt', 'w', encoding='UTF8') as file:
        file.write(enc_data)
    return print('Success!\nInformation was encrypted in caesar_enc.txt')


def dec_func_caesar(key: int) -> None:
    with open('caesar_enc.txt', 'r', encoding='UTF8') as file:
        line = list(file.readline())
        for i in range(len(line)):
            if line[i] in ascii_lowercase:
                symbol_index = ascii_lowercase.find(line[i])
                if symbol_index >= 0:
                    symbol_index = symbol_index - key
                    if symbol_index > (len(ascii_lowercase) - 1) or symbol_index < (len(ascii_lowercase) - 1) * (-1):
                        symbol_index = symbol_index % len(ascii_lowercase)
                    line[i] = ascii_lowercase[symbol_index]
            elif line[i] in ascii_uppercase:
                symbol_index = ascii_uppercase.find(line[i])
                if symbol_index >= 0:
                    symbol_index = symbol_index - key
                    if symbol_index > (len(ascii_uppercase) - 1) or symbol_index < (len(ascii_uppercase) - 1) * (-1):
                        symbol_index = symbol_index % len(ascii_uppercase)
                    line[i] = ascii_uppercase[symbol_index]
            elif line[i] in digits:
                symbol_index = digits.find(line[i])
                if symbol_index >= 0:
                    symbol_index = symbol_index - key
                    if symbol_index > (len(digits) - 1) or symbol_index < (len(digits) - 1) * (-1):
                        symbol_index = symbol_index % len(digits)
                    line[i] = digits[symbol_index]
            elif line[i] in punctuation:
                symbol_index = punctuation.find(line[i])
                if symbol_index >= 0:
                    symbol_index = symbol_index - key
                    if symbol_index > (len(punctuation) - 1) or symbol_index < (len(punctuation) - 1) * (-1):
                        symbol_index = symbol_index % len(punctuation)
                    line[i] = punctuation[symbol_index]
        enc_data = ''.join(line)
        print(enc_data)
    with open('caesar_enc.txt', 'w', encoding='UTF8') as file:
        file.write(enc_data)
    return print('Success!\nInformation was deciphered in caesar_enc.txt')


def menu_input():
    '''
    Creates console menu for user

    :return:
    '''

    while True:
        print('Type "1" if you want to create file')
        print('Type "2" if you want to create encrypted file')
        print('Type "3" if you want to decipher existing file')
        print('Type "-1" if you want to exit')
        num = input('What operation do you want to do?: ')
        if num == '1':
            file_create()
        elif num == '2':
            if path.exists(fr'.\caesar_enc.txt'):
                caesar_key = enc_key_caesar()
                enc_func_caesar(key=caesar_key)
            else:
                print('File caesar_enc.txt is not exist in this folder.')
                print("Would you like to create file? (Y/N)")
                if input().lower() in ('y', 'ye', 'yes'):
                    file_create()
                else:
                    print("Create file caesar_enc.txt and put it to root folder\n")
        elif num == '3':
            if path.exists(fr'.\caesar_enc.txt'):
                caesar_key = enc_key_caesar()
                dec_func_caesar(key=caesar_key)
            else:
                print('File caesar_enc.txt is not exist in this folder.')
                print("Would you like to create file? (Y/N)")
                if input().lower() in ('y', 'ye', 'yes'):
                    file_create()
                else:
                    print("Create file caesar_enc.txt and put it to root folder\n")
        elif num == '-1':
            return exit(print("Bye-bye"))
        else:
            print("Incorrect value, try again!")


menu_input()
