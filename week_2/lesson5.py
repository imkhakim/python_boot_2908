# #методы словарей
# kpi = {
#     "python": 90,
#     "java": 80,
#     "ux-ui": 55
# }
#
# new_kpi = kpi.copy()
# kpi["python"] = 95
# kpi["java"] = 98
#
# print(kpi)
# print(new_kpi)
#
# from copy import deepcopy
# kpi = {
#     "python": 90,
#     "java": 80,
#     "ux-ui": 55
# }
# new_kpi = deepcopy(kpi)
#
# kpi["python"] = 95
# kpi["java"] = 98
# print(kpi)
# print(new_kpi)
#
# #tuple/кортежи
#
# a = tuple()
# a, b = (1,2)
#
# print(a)
#
# a = (1, "dsdsffs", ["a", ])
# a[2].append("n")
#
# print(a)
#
# a = (1, "nazi", ("a", ))
# # a[2][0] = ("d")
#
# print(a)
#
# print(a.count(1))
# print(a.index(1))
#
# s = a.index
# print(s("nazi"))


# mas_a = [1, 2, 3]
# mas_b = [[1, 2], [1, 4], [1, 3]]
# mas_b[0][0] = 0
# print(mas_b)
#
# for i in mas_a:
#     print(pow(i, 2))
#
# for e, y in mas_b:
#     print(pow(e, 2), pow(y, 2))

# for e in mas_b:
#     for y in e:
#         print(y**2)

mas_c = [[1, 2, 3], [2, 3, 4], [5, 6, 7] ]

mas_c[0][0] = 0
mas_c[1][1] = 0
mas_c[2][2] = 0
print(mas_c)

for i in range(len(mas_c)):
    mas_c[i][i]
print(mas_c)

mas_d = [[1, 2, 4], [1, 4, 6], [1, 3, 2] ]
for i in range(len(mas_d)):
    for y in range(len(mas_d[i])):
        if i == y:
            mas_d[i][y] = 0
print(mas_d)

