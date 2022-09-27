# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
# *Пример:*
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day_number = int(input('Enter day number: '))
if day_number <= 0 or day_number > 7:
    print(f'{day_number} is not a day of a week!')
elif day_number in range(6,8):
    print("It's a weekend, let's party!")
else:
    print("Boooriiiing, it's not a weekend")

