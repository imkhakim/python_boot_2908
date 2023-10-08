#task1

'''Создайте класс BankAccount с атрибутом класса interest_rate и методами экземпляра deposit() и withdraw().
Метод deposit() увеличивает баланс на указанную сумму, а метод withdraw() уменьшает баланс.
При создании объекта этого класса, установите начальный баланс и процентную ставку.
Затем выполните несколько операций по депозиту и снятию средств, используя методы экземпляра, и выведите итоговый баланс.'''

class BankAccount:

    def __init__(self, interest_rate):

        self.interest_rate = interest_rate

    def deposit(self):
        deposit = self.interest_rate / 100 * self.balance
        self.balance = self.balance + deposit
        return self.balance

    def withdraw(self):
        withdraw = self.interest_rate / 100 * self.balance
        self.balance = self.balance - withdraw
        return self.balance

bill_1 = BankAccount(10)
bill_1.balance = 1000

(bill_1.deposit())
(bill_1.withdraw())
(bill_1.deposit())
print(bill_1.balance)


#task2

'''Создайте класс Rectangle, у которого есть атрибуты экземпляра width и height. 
Добавьте метод экземпляра calculate_area(), который возвращает площадь прямоугольника (ширина * высота).
Создайте объект этого класса и вызовите метод calculate_area().'''


class Rectangle:

    def __init__(self, width, height):

        self.width = width
        self.height = height

    def calculate_area(self):
        area = self.width * self.height
        return area

figure_1 = Rectangle(2, 3)
print(figure_1.calculate_area())


#task3

'''Создайте класс Counter, у которого есть атрибут экземпляра count со значением 0.
Добавьте методы increment() и decrement(), которые увеличивают и уменьшают значение атрибута count.
Создайте объект этого класса и вызовите методы для изменения значения count.'''

class Counter:

    def __init__(self, count=0):
        self.count = count

    def increment(self, number):
        self.count = self.count + number
        return self.count

    def decrement(self, number):
        self.count = self.count - number
        return self.count

count_1 = Counter()

print(count_1.increment(10))
print(count_1.decrement(5))
print(count_1.increment(15))
print(count_1.decrement(20))