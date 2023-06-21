
def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv("phonebook.csv")
    
    while (choice !=8):
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            name = input("Введите имя: ")
            print(find_by_name(phone_book, name))
        elif choice == 3:
            phone = input("Введите телефон: ")
            print(find_by_phone(phone_book, phone))
        elif choice == 4:
            user_data = get_new_user()
            add_user(phone_book, user_data)
            write_csv("phonebook.csv", phone_book)
        elif choice == 5:
            file_name = get_file_name()
            write_txt(file_name, phone_book)
        elif choice == 6:
            edit_contact(phone_book)
        elif choice == 7:
            delete_contact(phone_book)
        choice = show_menu()
        
def show_menu():
    print(  "Меню:\n"
            "1. Показать все контакты\n"
            "2. Найти контакт по имени\n"
            "3. Найти контакт по номеру телефона\n"
            "4. Добавить новый контакт\n"
            "5. Экспортировать контакты в текстовый файл\n"
            "6. Внесения изменений в книге\n"
            "7. Удаление абонента с книги\n"
            "8. Выход\n")
    choice = int(input("Выберите пункт: "))
    return choice

def read_csv(file_name):
    phone_book = []
    with open(file_name, "r", encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            surname, name, number, description = line.strip().split(",")
            phone_book.append({"Фамилия":surname, "Имя" : name, "Телефон" : number, "Описание" : description})
    return phone_book

def print_result(phone_book):
    if phone_book:
        for contact in phone_book:
            print("{}, {}, {}, {}".format(contact["Фамилия"], contact["Имя"],contact["Телефон"],contact["Описание"]))
    else:
        print("Телефонная книга пуста.")

def find_by_name(phone_book, name):
    found_contacts = []
    for contact in phone_book:
        if name in contact["Имя"]:
            found_contacts.append(contact)
    if found_contacts:
        print("Найденные контакты:")
        for contact in found_contacts:
            print("{}, {}, {}, {}".format(contact["Фамилия"], contact["Имя"],contact["Телефон"],contact["Описание"]))
    else:
        print("Контакты с таким именем не найдены.")
        
def find_by_phone(phone_book, phone):
    found_contacts = []
    for contact in phone_book:
        if phone in contact["Телефон"]:
            found_contacts.append(contact)
    if found_contacts:
        print("Найденные контакты:")
        for contact in found_contacts:
            print("{}, {}, {}, {}".format(contact["Фамилия"], contact["Имя"],contact["Телефон"],contact["Описание"]))
    else:
        print("Контакты с таким именем не найдены.")

def get_new_user():
    surname = input("Введите фамилию нового контакта: ")
    name = input("Введите имя нового контакта: ")
    number = input("Введите номер телефона нового контакта: ")
    description = input("Введите описание нового контакта: ")
    return {"Фамилия":surname, "Имя" : name, "Телефон" : number, "Описание" : description}

def add_user(phone_book, new_user):
    phone_book.append(new_user)
    print("Контакт успешно добавлен.")

def write_csv(file_name, phone_book):
    with open(file_name, "w", encoding='utf-8') as file:
        for contact in phone_book:
            file.write("{}, {}, {}, {} \n".format(contact["Фамилия"], contact["Имя"],contact["Телефон"],contact["Описание"]))

def get_file_name():
    file_name = input("Введите имя файла для экспорта: ")
    if not file_name.endswith(".txt"):
        file_name += ".txt"
    return file_name

def write_txt(file_name, phone_book):
    with open(file_name, "w") as file:
        if phone_book:
            for contact in phone_book:
                file.write("Фамилия: {}\n".format(contact["Фамилия"]))
                file.write("Имя: {}\n".format(contact["Имя"]))
                file.write("Телефон: {}\n".format(contact["Телефон"]))
                file.write("Описание: {}\n".format(contact["Описание"]))
                file.write("\n")
            print("Контакты успешно экспортированы в файл {}.".format(file_name))
        else:
            print("Телефонная книга пуста. Нечего экспортировать.")

def edit_contact(phone_book):
    last_name = input("Введите фамилию контакта, которого хотите изменить: ").strip()
    for contact in phone_book:
        if contact["Фамилия"].lower() == last_name.lower():
            print("Найден контакт:", contact)
            field = input("Введите название поля, которое хотите изменить (Фамилия, Имя, Телефон, Описание): ").strip().lower()
            if field in ["фамилия", "имя", "телефон", "описание"]:
                new_value = input("Введите новое значение: ").strip()
                contact[field.capitalize()] = new_value
                print("Контакт успешно изменен:")
                return
            else:
                print("Некорректное название поля.")
                return
    else:
        print("Контакт не найден.")

def delete_contact(phone_book):
    last_name = input("Введите фамилию контакта, которого хотите удалить: ").strip()
    for i, contact in enumerate(phone_book):
        if contact["Фамилия"].lower() == last_name.lower():
            print("Найден контакт:", contact)
            del phone_book[i]
            print("Контакт успешно удален.")
            return
    else:
        print("Контакт не найден.")

work_with_phonebook()