# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

num = input('Enter value for number: ')
force_to_int = len(num) - 2
num = int(float(num) * (10 ** force_to_int))
summ = 0
while num != 0:
    summ += num % 10
    num //= 10
print(f'Summary of digits: {summ}')
