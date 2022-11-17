import phone_book
import export_csv
import export_txt
import import_csv
import view

def import_export():
    phone_book.add_contact("Egor", "Zimov", "+7555555555", "musician")
    imported = import_csv.import_csv()
    phone_book.add_contacts(imported)
    view.show_contacts(phone_book.get_contacts())
    export_csv.export(phone_book.get_contacts())
    export_txt.export(phone_book.get_contacts())
