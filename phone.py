n = int(input("Введите кол-во телефонны"))  # количество номеров телефонов
phone_book = {}   # словарь для хранения номеров телефонов

# считываем номера телефонов и имена их владельцев
for i in range(n):
    phone, name = input().split()
    phone_book[name] = phone

# считываем запрос и выводим номер телефона
query = input("Введите имя ")
if query in phone_book:
    print(phone_book[query])
else:
    print("Нет в телефонной книге")