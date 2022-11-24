# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

num = float(input('Enter value for number: '))
summ = 0
fract_num = round(num - int(num), 8)
num = int(num)
while num != 0 or fract_num != int(fract_num):
    fract_num = round(fract_num * 10, 8)
 #   print(f'fract_num% = {int(fract_num % 10)}')
 #   print(f'num% = {num % 10}')
    summ += int(fract_num % 10) + num % 10
    num //= 10
 #   print(f'sum = {summ} num = {num} fract_num = {fract_num}')
 #   print
print(f'Digits summary: {summ}')
