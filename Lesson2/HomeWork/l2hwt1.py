# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Учтите, что числа могут быть отрицательными.
# Пример:
# 67.82 -> 23
# (-0.56) -> 11


num = input('Enter value for number: ').replace(',', '.')
force_to_int = len(num) - 1
try:
    num = abs(int(float(num) * (10 ** force_to_int)))
except ValueError:
    exit('Value is incorrect. Type a real number.')
summary = 0
while num != 0:
    summary += num % 10
    num //= 10
print(f'Summary of digits: {summary}')
