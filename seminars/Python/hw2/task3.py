# 3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

n = int(input('Введите число: '))
sum = 0
list = []

for i in range(1, n+1):
    current = (1+1/i)**i
    list.append(current)
    sum += current

print(list)
print(f'Сумма {n} чисел последовательности равна {round(sum, 2)}')
