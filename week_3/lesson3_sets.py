# set methods

set1 = {1, "nazi", 3, 4 }
set_2 = {1, 4, "nazi" }

# print(set1.isdisjoint(set_2))

# set1.add(2)
# print(set1)

# set_3 = set1.copy()
#
# print(id(set_3))
# print(id(set_2))

set1 = {1, "nazi", 3, 4 }
set_2 = {1, 4, "nazi" }

# print(set.difference(set_2))
# print(set.difference(set1))
#
# set1.difference_update(set_2)
# print(set1)
#
# set1.symmetric_difference(set_2)
# print(set1)
#
# print(set1.intersection(set_2))
# set1.intersection_update(set_2)
#
# print(set1)

# set1 = {1, "nazi", 3, 4 }
# set_2 = {1, 4, "nazi", 5 }
#
# print(set_2.issubset(set1))
# print(set_2.issuperset(set1))
#
# print(set_2.union(set1))
#
# set_2.discard(6)
# print(set_2)

# list1 = [1, 2, 3, 2, 1 ]
#
# print(len(set(list1)))


# list1 = [1, 2, 3, ]
# list2 = [1, 4, 5 ]
# set1 = set(list1).intersection(set(list2))
# print(set1)
# print(len(set1))

# set1 = {1, 10, 223, 413, 2}
# set2 = {1, 10, 223, 413, 2}
#
# print(set1.issubset(set2))

# numbers_list =  []
# for i in range(1, 101):
#     numbers_list.append(i)
# print(numbers_list)
#
# numbers_list_2 = []
# i = 100
# while i >= 1:
#     numbers_list_2.append(i)
#     i -= 1
# print(numbers_list_2)

# lists = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#
# i = 0
# while True:
#     print(lists[i])
#     if lists[i] == 90:
#         break
#     i += 1

spisok = [23, 76, 89, 76, 100, ]

new_list1 = []

i = 0
while i < len(spisok):
    if spisok[i] % 2 == 0:
        i += 1
        continue
    new_list1.append(spisok[i])
    i += 1
print(new_list1)

new_list2 = []
i = 0
while True:
    if i == len(spisok):
        break
    if spisok[i] % 2 == 0:
        i += 1
        continue
    new_list2.append(spisok[i])
    i += 1
print(new_list2)
