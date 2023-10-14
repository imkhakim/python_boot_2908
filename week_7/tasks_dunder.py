'''1) Создайте класс Playlist, представляющий плейлист с песнями.
Переопределите метод __str__, чтобы он выводил список песен в читаемом виде, и метод __len__,
чтобы можно было узнать количество песен в плейлисте.'''
class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __str__(self):
        return (f"{self.songs}")

    def __len__(self):
        return len(self.songs)

list_1 = Playlist(["Bad Karma", "Bailando", "I got love", "Suicidal"])

print(list_1)
print(len(list_1))

'''2) Создайте класс, который будет представлять собой неизменяемый объект, 
и переопределите методы __hash__ и __eq__, чтобы можно было использовать его в множествах и как ключи в словарях.'''

class Circle:

    def __init__(self, x, y, diameter):
        self.x = x
        self.y = y
        self.diameter = diameter

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.diameter == other.diameter

    def __hash__(self):
        return hash((self.x, self.y, self.diameter))

circ_1 = Circle(1, 2, 20)
circ_2 = Circle(1, 2, 20)

print(hash(circ_1))
print(hash(circ_2))

set_1 = {circ_1, circ_2}

print(set_1)

dict_1 = {}

dict_1[circ_1] = "a"
dict_1[circ_2] = "b"

print(dict_1)
