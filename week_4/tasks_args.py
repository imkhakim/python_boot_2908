#task1

'''Задача 1
Напишите функцию `max_value`, которая принимает произвольное число аргументов и
возвращает максимальное значение среди них.

Пример использования:
print(max_value(1, 2, 3, 4, 5))

Вывод: 5'''

def max_value(*args):
    print(max(args))

max_value(10, 1, 4001, 501, 7, 100)


'''Задача 2
Напишите функцию `merge_lists`, которая принимает произвольное число списков в виде аргументов *args
и возвращает новый список, содержащий все элементы этих списков.

Пример использования:
print(merge_lists([1, 2, 3], [4, 5], [6, 7, 8, 9]))
Вывод:
[1, 2, 3, 4, 5, 6, 7, 8, 9]'''

list_1 = []
def merge_lists(*args):
    for arg in args:
        list_1.extend(arg)

    print(list_1)

merge_lists([1, 2, 3], [4, 5], [6, 7, 8, 9])


'''Задача 3
Напишите функцию `print_user_data`, которая принимает произвольное число именованных аргументов **kwargs,
представляющих информацию о пользователе (имя, возраст, город и т.д.), и
выводит эту информацию в отформатированном виде.

Пример использования:
print_user_data(name="John", age=30, city="New York", occupation="Programmer")

Вывод:
Name: John
Age: 30
City: New York
Occupation: Programmer'''

def print_user_data(**kwargs):
    for key, value in kwargs.items():
        print("%s: %s" % (key.capitalize(), value))

print_user_data(name="John", age=30, city="New York", occupation="Programmer")
