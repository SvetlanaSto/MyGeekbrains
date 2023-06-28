def draw_tree(length):
    for i in range(1, length + 1):
        spaces = ' ' * (length - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

tree_length = int(input("Сколько рядов у ёлки? "))
draw_tree(tree_length)
