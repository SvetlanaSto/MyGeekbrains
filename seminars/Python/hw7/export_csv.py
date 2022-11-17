def export(contacts):
    with open('export.csv', 'w') as file:
        for first_name, last_name, phone, description in contacts:
            file.write(f"{first_name};{last_name};{phone};{description}\n")
