# Создание начального словаря
address_book = {
    "Иван Иванов": "ул. Ленина, д. 1",
    "Мария Смирнова": "ул. Октябрьская, д. 12",
    "Алексей Петров": "ул. Пушкина, д. 3"
}

# Основной цикл программы
while True:
    print("\nДействия:")
    print("1. Изменить адрес")
    print("2. Удалить запись")
    print("3. Просмотреть весь словарь")
    print("4. Выйти")
    action = input("Выберите действие (1-4): ")

    if action == "1":
        # Изменение адреса
        name = input("Введите имя человека, чей адрес хотите изменить: ")
        if name in address_book:
            new_address = input("Введите новый адрес: ")
            address_book[name] = new_address
            print(f"Адрес для {name} изменен на {new_address}.")
        else:
            print("Такого имени в словаре нет.")
    
    elif action == "2":
        # Удаление записи
        name = input("Введите имя человека, чью запись хотите удалить: ")
        if name in address_book:
            del address_book[name]
            print(f"Запись для {name} удалена.")
        else:
            print("Такого имени в словаре нет.")
    
    elif action == "3":
        # Просмотр всего словаря
        print("\nСловарь:")
        for name, address in address_book.items():
            print(f"{name}: {address}")

    elif action == "4":
        # Выход из программы
        print("Выход из программы.")
        break
    
    else:
        print("Неверное действие. Пожалуйста, выберите действие от 1 до 4.")

