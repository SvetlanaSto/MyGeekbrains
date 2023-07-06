# Пользователь вводит строку текста. Подсчитайте сколько раз встречается каждая буква в строке
# без использования метода count и с ним.
# Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
# Обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в ваших решениях.

def count1(string):
    letter_count = {}

    for char in string:
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

    return letter_count


def count2(string):
    letter_count = {}

    for char in set(string):
        if char.isalpha():
            letter_count[char] = string.count(char)

    return letter_count


string = input("Введите строку текста: ")
result1 = count1(string)
print("Частота встречи символов в строке (без использования count):", result1)

result2 = count2(string)
print("Частота встречи символов в строке (с использованием count):", result2)
