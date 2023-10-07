#task1, 2

'''Попросите пользователя ввести имя файла, а затем попытайтесь открыть этот файл для чтения.
Обработайте исключение, которое может возникнуть, если файл не существует.


Создайте программу, которая запрашивает у пользователя число и пытается найти квадратный корень этого числа.
Обработайте исключение, которое может возникнуть, если пользователь вводит отрицательное число.'''
import math

#task1
file_name_1 = input("Enter name of file:" )

try:
    open_file_1 = open(str(file_name_1), "r")

except FileNotFoundError as err:
    print("Error: Файла с таким именем не существует в проекте!")

#task2

number_1 = int(input("Enter number:" ))

try:
    square_number = math.sqrt(number_1)
    print(square_number)

except ValueError as err:
    print(" Error: Enter positive number")


