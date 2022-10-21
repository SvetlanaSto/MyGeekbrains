# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input('Введите количество элементов после нуля: '))

fibo = [0]
if n != 0:
    fibo.append(1)
    fibo.insert(0, 1)

    for i in range(n-1):
        fibo.append(fibo[-2] + fibo[-1])
        fibo.insert(0, fibo[1] - fibo[0])

print(fibo)