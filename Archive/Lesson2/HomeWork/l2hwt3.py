# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

num = int(input('Enter value for number: '))
formula = 1
result_list = list()
summ = 0
for i in range(1, num + 1):
    formula = int(round((1 + 1 / i) ** i, 0))
    result_list.append(formula)
    summ += formula
print(f'{result_list} -> {summ}')
