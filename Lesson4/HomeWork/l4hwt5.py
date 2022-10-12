# 5. ** Даны два файла, в каждом из которых находится запись многочленов.
# Задача - сформировать файл, содержащий сумму многочленов.
# in
# "poly.txt"
# "poly_2.txt"
#
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
# 4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0
from random import choice


def addition_from_file(file1, file2):
    with open(file1, 'r', encoding="UTF-8") as output1:
        with open(file2, 'r', encoding="UTF-8") as output2:
            if sum(1 for _ in open(file1, 'r')) == sum(1 for _ in open(file2, 'r')):
                with open("file1.txt", 'a', encoding="UTF-8") as output:
                    data1 = output1.readlines()
                    data2 = output2.readlines()
                    for i in range(len(data1)):
                        data1[i] = data1[i].strip('0\n').replace('=', choice(['+', '-'])) + data2[i]
                        output.write(data1[i])
            else:
                return "Data in files don't match!"


first_file = input('Enter name of the first file: ')
second_file = input('Enter name of the second file: ')
addition_from_file(first_file, second_file)
