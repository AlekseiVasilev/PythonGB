# 4. Напишите программу, которая будет принимать на вход дробь
# и показывать первую цифру дробной части числа.

n = float(input('Enter number: '))
result = n * 10 % 10
if result > 0:
    print(f'First digit of fractional part -> {int(result)}')
else:
    print('First digit of fractional part is not exist')

