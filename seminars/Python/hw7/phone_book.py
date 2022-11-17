contacts = []

def add_contact(first_name, last_name, phone, description):
    contacts.append((first_name, last_name, phone, description))

def add_contacts(data):
    contacts.extend(data)

def get_contacts():
    return contacts
