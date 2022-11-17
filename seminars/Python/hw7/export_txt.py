def export(contacts):
    with open('export.txt', 'w') as file:
        for first_name, last_name, phone, description in contacts:
            file.write(f"{first_name}\n")
            file.write(f"{last_name}\n")
            file.write(f"{phone}\n")
            file.write(f"{description}\n\n")
       