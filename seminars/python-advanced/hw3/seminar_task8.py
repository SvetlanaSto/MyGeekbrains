# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение —
# кортеж вещей.
# Ответьте на вопросы: Какие вещи взяли все три друга
# Какие вещи уникальны, есть только у одного друга
# Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

def find_unique_items(friends_items):
    all_items = []
    unique_items = []

    for items in friends_items.values():
        all_items += items

    for item in all_items:
        if all_items.count(item) == 1:
            unique_items.append(item)

    return set(unique_items)


friends = {
    'Пётр': ('Рюкзак', 'Спальник', 'Фонарик', 'Термос'),
    'Иван': ('Кружка', 'Фонарик', 'Котелок', 'Рюкзак'),
    'Егор': ('Вода', 'Фонарик', 'Спальник', 'Матрац', 'Рюкзак')
}

friend_items = {}
for friend, items in friends.items():
    friend_items[friend] = set(items)

common_items = set.intersection(*friend_items.values())
unique_items = find_unique_items(friends)
all_items = set.union(*friend_items.values())

print("Вещи, которые взяли все три друга:", common_items)
print("Уникальные вещи, которые есть только у одного друга:", unique_items)
print("Вещи, которые есть у всех друзей, кроме одного:", all_items - unique_items - common_items)
