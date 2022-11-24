# 4.* Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена,
# записать в файл полученный многочлен не менее 3-х раз.
# in
# 9
# 5
# 3
#
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0

from random import randint, choice


def random_list(listlen):
    datalist = list()
    for i in range(listlen):
        datalist.append(randint(0, 10))
    return datalist


def polynom_r_file(pow, doc_no):
    coeff = random_list(pow + 1)
    result_string = []
    with open(f"poly_{doc_no}.txt", "a", encoding="UTF-8") as output:
        for i in range(pow):
            if coeff[i] != 0:
                result_string.append(f"{coeff[i]}*x^{pow - i}")
        if coeff[-1] != 0:
            result_string.append(f"{coeff[i]}")
        for i in range(len(result_string) - 1):
            output.write(result_string[i])
            output.write(f' {choice(["+", "-"])} ')
        output.write(f'{result_string[-1]} = 0\n')


print('Enter power for polynom: ')
k = int(input('k = '))
if k < 1:
    quit()
doc = input('Enter # for the document: ')
polynom_r_file(k, doc)
