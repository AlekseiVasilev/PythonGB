# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# - 4 -> [1, 2, 6, 24]
# - 6 -> [1, 2, 6, 24, 120, 720]

num = int(input('Enter value for number: '))
factorial = 1
result_list = list()
if num == 0 or num == 1:
    print(f'{num}! = 1')
elif num > 1:
    for i in range(1, num + 1):
        factorial *= i
        result_list.append(factorial)
    print(f'{num}! = {result_list}')
else:
    print('Value is incorrect, function exist only for positive integer numbers')
