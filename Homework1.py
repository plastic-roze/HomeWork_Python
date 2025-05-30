def show_menu():
    print("╔══════════════════════════╗")
    print("║        HomeWork #1       ║")
    print("╠══════════════════════════╣")
    print("║ 1. Форматирование строк  ║")
    print("║ 2. Четность числа        ║")
    print("║ 3. Проверка возраста     ║")
    print("║ 4. Длина числа           ║")
    print("║ 5. Выход                 ║")
    print("╚══════════════════════════╝")

def main():
    while True:
        show_menu()
        choice = input("Выберите пункт (1-5): ")
        
        if choice == "1":
            print("\n--- Форматирование строк ---")
            first_name = input("Введите имя: ")
            last_name = input("Введите фамилию: ")
            age = input("Ваш возраст: ")
            
            # Вариант с format
            output_format = "Ваше имя: {}, Фамилия: {}, Возраст: {} лет".format(
                first_name, last_name, age
            )
            print("\nРеализация через format:")
            print(output_format)
            
            # Вариант с f-строкой
            output_fstring = f"Ваше имя: {first_name}, Фамилия: {last_name}, Возраст: {age} лет"
            print("\nРеализация через f-string:")
            print(output_fstring)
            
        elif choice == "2":
            print("\n--- Проверка четности числа ---")
            while True:
                user_input = input("Введите число (или 'назад' для возврата): ")
                if user_input.lower() == 'назад':
                    break
                if user_input.lstrip('-').isdigit():
                    number = int(user_input)
                    if number % 2 == 0:
                        print(f"Число {number} является четным")
                    else:
                        print(f"Число {number} не является четным")
                else:
                    print("Ошибка: введено не число")
        
        elif choice == "3":
            print("\n--- Проверка возраста ---")
            while True:
                user_input = input("Введите ваш возраст (или 'назад' для возврата): ")
                if user_input.lower() == 'назад':
                    break
                if user_input.isdigit():
                    age = int(user_input)
                    if age < 0:
                        print("Ошибка: возраст не может быть отрицательным!")
                    elif age >= 18:
                        print("Вы совершеннолетний.")
                    else:
                        print("Вы несовершеннолетний.")
                else:
                    print("Ошибка: введено не число!")
        
        elif choice == "4":
            print("\n--- Определение длины числа ---")
            while True:
                user_input = input("Введите число (или 'назад' для возврата): ")
                if user_input.lower() == 'назад':
                    break
                if user_input.lstrip('-').isdigit():
                    number = user_input.lstrip('-')
                    print(f"В этом числе {len(number)} цифр(а/ы).")
                else:
                    print("Ошибка: данные не являются числом.")
        
        elif choice == "5":
            print("\nВыход из программы...")
            break
            
        else:
            print("\nОшибка: выберите пункт от 1 до 5")

if __name__ == "__main__":
    main()5