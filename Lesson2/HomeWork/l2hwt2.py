# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.


try:
    num = int(input('Enter value for number: '))
except ValueError:
    exit('Value is incorrect. Type natural number')
factorial = 1
result_list = list()
if num == 0:
    result_list.append(1)
    print(f'{num}! = {result_list}')
elif num >= 1:
    for i in range(1, num + 1):
        factorial *= i
        result_list.append(factorial)
    print(f'{num}! = {result_list}')
else:
    print('Value is incorrect, function exist only for positive integer numbers')
