
# contacts = ["Nazgul", "Beka", "Talant"]
# new_contacts = []
# for i in contacts:
#     new_contacts.append (i.upper())
# print(new_contacts)

# for i in contacts:
#     new_contacts.append (len(i))
# print(new_contacts)

# 1) Создать список своих любимых фильмов. Вывести список тремя способами:
# а) в строчку; б) в столбик; в) в строчку через запятую.

films = ["1+1", "Жизнь Пи", "Бакуган"]

print("".join(films))

for i in films:
    print(i)

print(", ".join(films))

# 2) Ввести с клавиатуры список фамилий писателей. Отсортировать список в алфавитном порядке и вывести его.

last_names = []
for i in range(3):
    last_names.append(input("Введите фамилию писателя:"))
last_names.sort()
print(last_names)

# 3) Создать список из пяти элементов. Заполнить его случайными числами.
# Вывести этот список. Найти и вывести сумму его элементов.

list_3 = [26, 55, 58, 25, 56]

summ_of_elements = sum(list_3)
print(summ_of_elements)

summ = 0
for number in list_3:
    summ += number
print(summ)

# 4) Создать список из десяти элементов.
# Заполнить его случайными числами.
# Вывести этот список. Вывести наибольший элемент списка.

list_4 = [26, 55, 58, 25, 56, 55, 101, 88, 93]

print(max(list_4))

# 5) Создать список из десяти элементов. Заполнить его случайными числами.
# Заменить все нечетные числа нулями. Вывести исходный и получившийся списки.
list_5 = [26, 55, 58, 25, 56, 55, 101, 88, 93]
task_5 = []
for i in list_5:
    if i % 2 != 0:
        task_5.append(i)
print(task_5)

