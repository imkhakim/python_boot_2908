
'''Напишите программу, содержащую список из десяти слов, в некоторых из которых есть повторяющиеся буквы, а в
некоторых нет. Напишите программу, которая выбирает случайное слово из списка, не содержащее повторяющихся букв.'''

list_1 = ["яблоко", "груша", "банан", "кокос", "помело", "киви", "слива", "апельсин", "персик", "авокадо", "вваа" ]

# print(len(list_1))

import random

word = random.choice(list_1)

seen_letter = ""

# for letter in word:
#     print(seen_letter)
#     if letter not in seen_letter:
#         print(f"{letter}: {word.count(letter)}")
#         seen_letter += letter
#
# print(word)

#генераторы списков
start_date = datetime.now()
empty_list = []
for i in range(50):
    empty_list.append(random.randint(100, 1000))
end_date = datetime.now() - start_date

start_date = datetime.now()
empty_list_2 = [random.randint(100, 1000) for i in range(50)]

end_date = datetime.now() - start_date