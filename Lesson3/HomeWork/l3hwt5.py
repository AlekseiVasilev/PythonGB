# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.


def neg_fibo_pos(number):
    np_fibo = [1, 0, 1]
    fib1 = fib2 = 1
    neg = -1
    for i in range(2, number + 1):
        fib1, fib2 = fib2, fib1 + fib2
        np_fibo.append(fib1)
        np_fibo.insert(0, neg * fib1)
        neg *= -1
    return np_fibo


num = int(input("Type amount of Fibonacci's/Negafibonacci's elements: "))
print(neg_fibo_pos(num))
