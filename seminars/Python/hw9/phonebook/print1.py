def print_all_to_bot():
    lines = []
    with open('employees.csv', encoding="utf-8") as data:
        for line in data:
            lines.append(line.replace(',', ' '))
    return '\n'.join(lines)
