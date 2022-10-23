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
from itertools import starmap, groupby


def file_system():
    doc_name = input("Enter the name of the file with the text: ")
    doc_rec = input("Enter the file name to record: ")
    doc_coded = input("Enter the name of the file to decode: ")
    with open(f"{doc_name}", "w", encoding="UTF-8") as output:
        with open(f"{doc_rec}", "w", encoding="UTF-8"):
            with open(f"{doc_name}", "w", encoding="UTF-8"):
                output.write(input('Enter some text: '))
    data = [doc_name, doc_rec, doc_coded]
    return data


def crypt_rle(strng_start, strng_crypt):
    if path.exists(fr'.\{strng_start}') and path.exists(fr'.\{strng_crypt}'):
        with open(strng_start, 'r', encoding="UTF-8") as no_code_rle:
            with open(strng_crypt, 'a', encoding="UTF-8") as code_rle:
                nocode_data = list(no_code_rle.readline())
                for i, j in groupby(nocode_data):
                    code_rle.write(str(len(list(j))) + str(i))
        return "Success!"
    else:
        return "Looks like some files don't exist!"


data_fs = file_system()
print(crypt_rle(data_fs[0], data_fs[1]))
