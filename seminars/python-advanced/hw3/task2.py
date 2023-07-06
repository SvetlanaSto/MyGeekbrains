# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии
# или из документации к языку.

def count_most_frequent_words(text):
    word_counts = {}

    cleaned_text = ''.join(char.lower() for char in text if char.isalnum() or char.isspace())

    words = cleaned_text.split()
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
#    print(word_counts)
    most_frequent_words = sorted(word_counts, key=word_counts.get, reverse=True)[:10]
    return most_frequent_words

input_text = "Манул, также палласов кот (лат. Otocolobus manul), — хищное млекопитающее семейства кошачьих. " \
             "Внешностью и размерами похож на домашнюю кошку, но отличается более короткими массивными " \
             "туловищем и лапами, а также длинным густым мехом. Длина головы и туловища составляет " \
             "от 46 до 65 см, длина хвоста — от 21 до 31 см, масса составляет 2—5 кг. Мех манула, " \
             "являющийся самым пушистым и густым среди кошачьих, имеет характерный неравномерный окрас, " \
             "причём основу в нём обычно составляет серый цвет, от более тёмного до более светлого, а также " \
             "примесь рыжеватого или охристого."
result = count_most_frequent_words(input_text)
print(result)
