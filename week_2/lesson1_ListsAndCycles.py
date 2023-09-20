# lists = [1, 2, 4 ,65, 4, ]
# print(lists[4])
#
# lists = []
# lists_1 = list()
#
# print(type(lists))
# print(type(lists_1))
#
# lists[0] = 8

# print(len(lists))

# swap_list = ["name", False, 1.9, 33]
# lists = [1, 2, 4 ,65, 4, ]
#
# new_list = swap_list * 2
#
# print(new_list)

# for i in range(1, 101, ):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)

# print(dir([]))

# empty_list = [12]
# empty_list.append("name")
#
# empty_list.insert(0, "surname")
#
# print(empty_list)

list_fruits = ["banana", "apple", "pineapple", ]
# print(list_fruits.index("apple"))

# list_fruits.sort()

# list_fruits.reverse()
#
# print(list_fruits.count("apple"))
#
# new_list = list_fruits.copy()
#
# new_list.append("kiwi")
#
# print(new_list)
# print(list_fruits)

# full_name = input("Введите ФИО:")
# my_list = full_name.split()
#
# print(my_list)

# full_name = ("Махиев,Хаким,Назирович")
# my_list = full_name.split(",", maxsplit = 1)
#
# print(my_list)

phone_numbers = ("996550568852,996707586521,996770528654,25456,996990526254")

mega = []
oshka = []
beeline = []

for i in phone_numbers.split(","):
    if len(i) == 12 and i.startswith("99655"):
        mega.append(i)
    elif len(i) == 12 and i.startswith("99670"):
        oshka.append(i)
    elif len(i) == 12 and i.startswith("99677"):
        beeline.append(i)
    elif len(i) != 12:
        print("Введено неверное количество символов")
    else:
        print("Оператора с номером:" + i + " не существует")

print(mega)
print(oshka)
print(beeline)