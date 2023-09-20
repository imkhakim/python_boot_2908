#task1
'''Задача 1
Напишите функцию с именем add_excitement, которая берет список строк и добавляет восклицательный знак (!)
в конец каждой строки в списке.
(а) Программа должна изменить исходный список и ничего не возвращать.
(b) Напишите ту же функцию, за исключением того, что она не должна изменять исходный список а вместо этого должна
возвращать новый список.'''

list_1 = ["dfdgs", "sfsfg", "fsfsf", "fsfsdg", "hrgdf" ]

def add_excitement_a(list, symbol):
    for i in range(len(list)):
        list[i] = list[i] + symbol
    return list

print(add_excitement_a(list_1, "!"))

list_a = ["dfdgs", "sfsfg", "fsfsf", "fsfsdg", "hrgdf" ]
list_b = []

def add_excitement_b(list, symbol):
    for i in range(len(list)):
        list[i] = list[i] + symbol
        list_b.append(list[i])
    return list_b

print(add_excitement_b(list_a, "!"))

#task2
'''Задача 2
Напишите функцию match, которая принимает две строки в качестве аргументов и возвращает
количество совпадений между строками. Совпадение — это когда две строки имеют один и тот же
символ с одним и тем же индексом. Например, «python» и «path» совпадают в первом, третьем и
четвертом символах, поэтому функция должна вернуть 3.'''

def match(str_1, str_2):
    list_2 =[]
    for i in str_1:
        for j in str_2:
            if i == j:
                list_2.append(i)
    print(len(list_2))

match("python", "path")

#task3

'''Задача 3 
Напомним, что если s является строкой, то s.find('a') найдет расположение первого символа a в s. 
Проблема в том, что он не находит местоположение каждого a. 
Напишите функцию findall, которая по 
заданной строке и одному символу возвращает список, содержащий все местоположения этого символа в строке. 
Он должен возвращать пустой список, если в строке нет вхождений символа.'''

def findall(str_1, symbol):

    list_index = []
    start = -1
    count = 0

    while True:
        start = str_1.find(symbol, start + 1)
        if start == -1:
            break
        list_index.append(start)

    print(list_index)

findall("banana", "a")