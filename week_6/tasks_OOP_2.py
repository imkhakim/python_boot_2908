#task1

'''Создайте систему классов для электронной библиотеки.
У вас должен быть базовый класс Item для представления элементов библиотеки (например, книг и видео),
с атрибутами, такими как title, author, и year. Создайте подклассы для разных типов элементов (например, Book и Video),
которые будут наследовать от базового класса Item. Реализуйте инкапсуляцию, чтобы контролировать доступ к атрибутам,
и добавьте методы для вывода информации о каждом элементе.'''

class Item:

    def __init__(self, title, author, year):
        self.title = title
        self._author = author
        self.__year = year

    def item_info(self):
        print(self.title + ", " + self._author)

    def get_year(self):
        print(self.__year)

class Book(Item):
    pass
class Video(Item):
    pass

book_1 = Book("Words in our life", "John Sandy", 1986)
video_1 = Video("My animals", "Sam Hennesy", 2020)

book_1.item_info()
book_1.get_year()
video_1.item_info()
video_1.get_year()

# print(book_1.title)
# print(book_1._author)
# print(book_1._Item__year)


#task2

'''Создайте систему классов для представления заказов в интернет-магазине.
Создайте класс Product с атрибутами, такими как name, price, и quantity.
Затем создайте класс Order, который может содержать несколько
экземпляров Product. Реализуйте методы для добавления и удаления товаров
из заказа, а также для вычисления общей суммы заказа.'''


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Order(Product):

    def __init__(self, list_1):
        self.list_1 = list_1

    def add_product(self, product):
        product_list_1.append(product)

    def remove_product(self, product):
        product_list_1.remove(product)

    def count_price(self, product_list):
         order = []
         for product in product_list:
             order.append(product.price * product.quantity)

         print(sum(order))

product_1 = Product("Book", 10, 2)    #создание объектов класса Product
product_2 = Product("T-shirt", 15, 1)
product_3 = Product("Chess", 20, 3)

product_list_1 = []
product_order = Order(product_list_1)  #создание объекта(список) класса Order

product_order.add_product(product_1)   #добавление объектов класса Product в список-(объект) класса Order
product_order.add_product(product_3)
product_order.add_product(product_2)

product_order.remove_product(product_3)  #удаление объектов класса Product из списока-(объекта) класса Order

product_order.count_price(product_list_1)  #вычисление общей стоимости заказа















