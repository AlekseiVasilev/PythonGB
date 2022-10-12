# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0,
# с помощью дополнительных библиотек python. Запросите значения А, В, С 3 раза.
# Уравнения и корни запишите в файл.

from math import sqrt

print('Enter coefficients for function:')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

discr = b ** 2 - 4 * a * c

with open("l4t2.txt", "a", encoding="UTF-8") as output:
    output.write(f"Function: {a}*x^2 + {b}*x + {c} = 0\n")
    if discr > 0 and a:
        x1 = (-b + sqrt(discr)) / (2 * a)
        x2 = (-b - sqrt(discr)) / (2 * a)
        output.write(f"First root: {x1}\n")
        output.write(f"Second root: {x2}\n")
    elif discr == 0:
        x1 = (-b) / (2 * a)
        output.write(f"One root: {x1}\n")
    else:
        output.write("There are no answers\n")
