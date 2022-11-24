# 5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21

def neg_fibo_pos(number):
    np_fibo = [1, 0, 1]
    fib1 = fib2 = 1
    neg = -1
    for i in range(2, number+1):
        fib1, fib2 = fib2, fib1 + fib2
        np_fibo.append(fib1)
        np_fibo.insert(0, neg * fib1)
        neg *= -1
    return np_fibo


num = int(input("Type amount of Fibonacci's/Negafibonacci's elements: "))
print(neg_fibo_pos(num))
