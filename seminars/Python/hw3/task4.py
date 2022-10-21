# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

dec = int(input('Введите число: '))
bin = ''
 
while dec > 0:
    cur_digit = str(dec % 2)
    bin = cur_digit + bin
    dec = int(dec / 2)

print(bin)
