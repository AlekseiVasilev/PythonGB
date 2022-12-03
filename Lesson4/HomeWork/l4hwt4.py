# 4- Шифр Цезаря - это способ шифрования,
# где каждая буква смещается на определенное количество символов влево или вправо.
# При расшифровке происходит обратная операция. Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст,
# а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.

from string import *


def file_create() -> None:
    '''
    Creates .txt file with text encrypted by caesar encription key.

    :return: info about operation
    '''

    with open('caesar_enc.txt', 'w', encoding='UTF8') as file:
        input_string = input("Type any information you wan't:\n>> ")
        file.write(input_string)
    return print("Success!\nYou have created caesar_enc.txt\n")


def enc_key_caesar() -> int:
    enc_key = []
    while True:
        key = input('Type key for caesar encryption.\n'
                    'For ex.: 2L - 2 symbols left, 3R - 3 symbols right\n'
                    '>> ').lower()
        if key[0].isdigit() and key[1].isdigit():
            enc_key.append(key[0] + key[1])
            enc_key.append(key[2])
        else:
            enc_key = list(key)
        if len(enc_key) > 2 or not enc_key[0].isdigit() or not enc_key[1] in ('r', 'l'):
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
                    line[i] = ascii_lowercase[symbol_index]
            elif line[i] in ascii_uppercase:
                symbol_index = ascii_uppercase.find(line[i])
                if symbol_index >= 0:
                    symbol_index = symbol_index + key
                    line[i] = ascii_uppercase[symbol_index]
            elif line[i] in digits:
                symbol_index = digits.find(line[i])
                if symbol_index >= 0:
                    symbol_index = symbol_index + key
                    line[i] = digits[symbol_index]
            if line[i] in punctuation:
                symbol_index = punctuation.find(line[i])
                if symbol_index >= 0:
                    symbol_index = symbol_index + key
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
                    line[i] = ascii_lowercase[symbol_index]
            elif line[i] in ascii_uppercase:
                symbol_index = ascii_uppercase.find(line[i])
                if symbol_index >= 0:
                    symbol_index = symbol_index - key
                    line[i] = ascii_uppercase[symbol_index]
            elif line[i] in digits:
                symbol_index = digits.find(line[i])
                if symbol_index >= 0:
                    symbol_index = symbol_index - key
                    line[i] = digits[symbol_index]
            if line[i] in punctuation:
                symbol_index = punctuation.find(line[i])
                if symbol_index >= 0:
                    symbol_index = symbol_index - key
                    line[i] = punctuation[symbol_index]
        enc_data = ''.join(line)
        print(enc_data)
    with open('caesar_enc.txt', 'w', encoding='UTF8') as file:
        file.write(enc_data)
    return print('Success!\nInformation was deciphered in caesar_enc.txt')


file_create()
key_enc = enc_key_caesar()
enc_func_caesar(key=key_enc)
dec_func_caesar(key=key_enc)
