def show_menu():
    print("╔════════════════════════════════╗")
    print("║            HomeWork #2         ║")
    print("╠════════════════════════════════╣")
    print("║ 1. Возведение в степень        ║")
    print("║ 2. Преобразование словаря      ║")
    print("║ 3. Пересечение двух списков    ║")
    print("║ 4. Подсчет количества слов     ║")
    print("║ 5. Выход                       ║")
    print("╚════════════════════════════════╝")

def main():
    while True:
        show_menu()
        choice = input("Выберите пункт (1-5): ")
        
        if choice == "1":
            nums = input("Введите числа через пробел: ").split()
            power = int(input("Введите степень: "))
            result = []
            for item in nums:
                if item.lstrip('-').isdigit():
                    result.append(str(int(item) ** power))
                else:
                    result.append(item * power)
            print("Вывод:", " ".join(result))
            
        elif choice == "2":
            dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}
            keys_set = set(dct.keys())
            values_set = set(dct.values())
            union_set = keys_set.union(values_set)
            print("Множество ключей:", keys_set)
            print("Множество значений:", values_set)
            print("Объединение множеств:", union_set)
        
        elif choice == "3":
            list1 = list(map(int, input("Введите первый список: ").split()))
            list2 = list(map(int, input("Введите второй список: ").split()))
            common_elements = set(list1) & set(list2)
            print("Общие элементы:", ' '.join(map(str, common_elements)))
        elif choice == "4":
            text = input("Введите строку: ").lower().split()
            unique_words = set(text)
            for word in unique_words:
                print(f"{word}: {text.count(word)}")
        elif choice == "5":
            print("\nВыход из программы...")
            break
            
        else:
            print("\nОшибка: выберите пункт от 1 до 5")

if __name__ == "__main__":
    main()