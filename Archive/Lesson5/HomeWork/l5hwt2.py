# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'
#
# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaavvvvvvvvvvvbbwwPPuuuTTYyWWQQ
#
# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaavbbwwPPuuuTTYyWWQQ
#
# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a11v2b2w2P3u2T1Y1y2W2Q

from os import path
from itertools import groupby


def file_system():
    doc_name = input("Enter the name of the file with the text: ")
    doc_rec = input("Enter the file name to record: ")
    doc_coded = input("Enter the name of the file to decode: ")
    data = [doc_name, doc_rec, doc_coded]
    return data


def choice_op(file1, file2, file3):
    print('What operation do you want to do?\n')
    print('Type "1" if you want to add some text')
    print('Type "2" if you want to crypt text')
    print('Type "3" if you want to decrypt text')
    print('Type "-1" if you want to exit')
    num = int(input('Choice: '))
    if num == 1:
        with open(f"{file1}", "w", encoding="UTF-8") as output:
            output.write(input('Enter some text: '))
    elif num == 2:
        print(crypt_rle(file1, file2))
    elif num == 3:
        print(decrypt_rle(file2, file3))
    elif num == -1:
        return exit(print("Bye-bye"))
    return "Incorrect value, try again!"


def crypt_rle(strng_start, strng_crypt):
    if path.exists(fr'.\{strng_start}') and path.exists(fr'.\{strng_crypt}'):
        with open(strng_start, 'r', encoding="UTF-8") as no_code_rle:
            with open(strng_crypt, 'w', encoding="UTF-8") as code_rle:
                nocode_data = list(no_code_rle.readline())
                for i, j in groupby(nocode_data):
                    code_rle.write(str(len(list(j))) + str(i))
        return "Success!"
    else:
        return "Looks like some files don't exist!"


def decrypt_rle(strng_crypt, strng_decrypt):
    if path.exists(fr'.\{strng_crypt}') and path.exists(fr'.\{strng_decrypt}'):
        with open(strng_crypt, 'r', encoding="UTF-8") as code_rle:
            with open(strng_decrypt, 'w', encoding="UTF-8") as no_code_rle:
                code_data = code_rle.readline()
                temp_ls = [code_data[0]]
                k = 0
                for i in range(1, len(code_data)):
                    if code_data[i].isdigit():
                        temp_ls[k] += code_data[i]
                    else:
                        temp_ls.append(code_data[i])
                        temp_ls.append("")
                        no_code_rle.write(f'{int(temp_ls[k]) * temp_ls[k + 1]}')
                        k += 2
        return "Success!"
    else:
        return "Looks like some files don't exist!"


data = file_system()
while True:
    choice_op(data[0], data[1], data[2])
