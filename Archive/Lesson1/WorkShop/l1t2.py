# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

max_val = 0
for i in range(5):
    print(f"Enter {i+1} value")
    val = int(input())
    if val > max_val:
        max_val = val
print(f"Maximum value is {max_val}")
