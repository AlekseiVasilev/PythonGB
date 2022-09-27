# 1. Напишите программу, которая принимает на вход два числа
# и проверяет, является ли одно число квадратом другого

a = int(input('Enter value of first number: '))
b = int(input('Enter value of second number: '))
if a ** 2 == b or b ** 2 == a:
    print('Yes')
else:
    print('No')
