#task1

'''Задача 1
Напишите декоратор, который проверяет, что результат функции является
числом, и возвращает его. Если результат не является числом, декоратор
должен вернуть None.

Пример:
@check_type
def my_func():
    return 42
result = my_func()
print(result) # 42

@check_type
def my_func():
    return "Hello, world!"
 result = my_func()
print(result) # None.'''

def decor_check_type(func):
    def wrapper():
        if (type(func())==int):
            print(func())
        elif (type(func())!=int):
            print("None")
    return wrapper

@decor_check_type
def my_func():
    return 42

my_func()
@decor_check_type
def my_func():
    return "Hello, world!"

my_func()


'''Задача 2
Напишите декоратор, который добавляет к результату функции префикс и суффикс.
Префикс и суффикс должны задаваться при вызове декоратора.

Пример:
@add_prefix_suffix("Result: ", "!")
def my_func():
    return "Hello, world"
result = my_func()
print(result) # Result: Hello, world!'''

def decor_add_prefix_suffix(func):
    def wrapper(prefix, suffix):
        print(prefix + " " + func() + suffix)
    return wrapper

@decor_add_prefix_suffix

def my_func():
    return "Hello, world"

my_func("Result:", "!")

