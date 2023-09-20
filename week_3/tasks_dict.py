#task1

'''Задача 1
Напишите программу, которая постоянно просит пользователя ввести названия продуктов и цены.

Эта программа предназначена для создания словаря продуктов и их цен.
Она будет запрашивать у пользователя названия продуктов и цены и сохранять их в словаре,
где названия продуктов будут ключами, а цены - значениями.
После того, как пользователь закончит вводить продукты и цены,
программа будет позволять им повторно вводить названия продуктов и
выводить соответствующую цену или сообщение, если товара нет в словаре.'''

dict_1 = {}

while True:
    key = input("Введите название продукта:")
    if key == "stop":
        break
    value = int(input("Введите цену продукта:"))

    dict_1[key] = value

print(dict_1)

while True:
    ask_product = input("Введите название продукта:")
    #print(dict_1.get(ask_product, "Такого продукта нет!"))
    if ask_product == "stop":
        break
    print(dict_1.get(ask_product, "Такого продукта нет!"))


# #task2

'''Задача 2
Используя словарь, созданный в предыдущей задаче, попросите пользователя ввести сумму
и распечатайте все товары, цена которых меньше этой суммы.'''

max_price = int(input("Введите максимально возможную цену:"))

list_1 = []

for key, value in dict_1.items():
    if value < max_price:
        list_1.append(key)

print(list_1)


#task3

'''Задача 3
Напишите программу которая использует словарь, где ключами являются названия месяцев,
а значениями - количество дней в каждом месяце.
(a) Программа запрашивает у пользователя название месяца и выводит количество дней,
находящихся в этом месяце, используя словарь.

(b) Все ключи словаря выводятся в алфавитном порядке.

(c) Программа выводит все месяцы, в которых 31 день.

(d) Пары (ключ-значение) выводятся в порядке возрастания количества дней в каждом месяцев.'''

# dict_2 = {"january": 31, "february": 28, "march": 31, "april": 30, "may": 31, "june": 30,
#           "july": 31, "august": 30, "september": 31, "october": 30, "november": 31,
#           "december": 31 }

from datetime import datetime
from calendar import month_name
from calendar import monthrange

month_name_list = []
month_num_day_list = []

current_year = datetime.now().year

for name in month_name:
    month_name_list.append(name)
month_name_list.remove("")
# print(month_name_list)

for month in range(1, 13):
    num_days = monthrange(current_year, month)[1]
    month_num_day_list.append(num_days)
# print(month_num_day_list)

dict_2 = dict(zip(month_name_list, month_num_day_list))

print(dict_2)

#task3 a)
'''(a) Программа запрашивает у пользователя название месяца и выводит количество дней,
находящихся в этом месяце, используя словарь.'''

a = input("Введите имя месяца:").capitalize()
print(dict_2[a])

#task3 b)
'''(b) Все ключи словаря выводятся в алфавитном порядке.'''

print(sorted(dict_2.keys()))

#task3 c)
'''(c) Программа выводит все месяцы, в которых 31 день.'''

month_31day = []

for key, value in dict_2.items():
    if value == 31:
        month_31day.append(key)
print(month_31day)

#task3 d)
'''(d) Пары (ключ-значение) выводятся в порядке возрастания количества дней в каждом месяцев.'''

sorted_values = sorted(dict_2.values())
sorted_dict_2 = {}

for i in sorted_values:
    for key in dict_2.keys():
        if dict_2[key] == i:
            sorted_dict_2[key] = dict_2[key]
print(sorted_dict_2)


#task4
'''Задача 4
Напишите программу которая использует словарь, который содержит десять имен пользователей и соответствующие пароли.
При запуске, она запрашивает у пользователя имя пользователя и пароль.

Если имя пользователя отсутствует в словаре, программа сообщает, что человек не является действительным 
пользователем системы.

Если имя пользователя есть в словаре, но пароль неверный, программа сообщает, что пароль недействителен.

Если имя пользователя и пароль верные, программа сообщает, что пользователь вошел в систему.'''


dict_3 = {"bek": "bek1", "gek": "gek1", "zek": "zek1", "jack": "jack1", "frog": 12345, 0000: 1234, 1111: "aaaa",
          "aabb": 7125, 3e83: "da34", 1111: 9999}

username = input("Введите имя пользователя:")
password = input("Введите пароль:")

if username not in dict_3.keys():
    print("Пользователя с таким именем не существует!")
elif password not in dict_3.values():
    print("Введен неверный пароль!")
else:
    print("Вы вошли в систему!")