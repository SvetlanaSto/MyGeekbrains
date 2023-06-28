num = int(input("Введите число: "))
if num <= 0 or num > 100000:
    print("Число должно быть положительным и не больше 100000")
else:
    if num == 1:
        print("1 не считается простым или составным числом")
    else:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, " - простое число")
        else:
            print(num, " - составное число")