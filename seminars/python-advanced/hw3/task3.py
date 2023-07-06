# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
def select_items(backpack_capacity, items):
    selected_items = {}
    remaining_capacity = backpack_capacity

    sorted_items = sorted(items.items(), key=lambda x: x[1])

    for item, weight in sorted_items:
        if weight <= remaining_capacity:
            selected_items[item] = weight
            remaining_capacity -= weight

    return selected_items

max_capacity = 15
items = {
    'Кружка': 1,
    'Фонарик': 2,
    'Куртка': 4,
    'Спальный мешок': 3,
    'Еда': 5,
    'Вода': 6,
}
result = select_items(max_capacity, items)
print(result)
