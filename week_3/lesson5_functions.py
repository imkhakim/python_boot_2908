#functions

# def first_func():
#     print("hello")
#
# first_func()

# first = [23323, 4443, 555, 5566, 55555, 643234, 32123 ]
# persent = 0.4
# total_summ = sum(first)
# my_money = total_summ - total_summ * persent
# print(my_money)
#
# def my_salary(dohod: list, persent: float = 0.4):
#     total_summ = sum(dohod)
#     my_money = total_summ - total_summ * persent
#     return my_money
#
# print(my_salary(first, persent))
# print(my_salary(first))
# print(my_salary(first, 0.1))
#
# def empty(a):
#     result = a + 3
#     print(a)
#     return result
# a = empty(2)
# print(a)

# def computepay(hours, stavka):
#     norm_hours = hours // 40 * 40
#     extra_hours = hours % 40
#     result = norm_hours * stavka + extra_hours * stavka * 1.5
#     return result
# print(computepay(45, 10))


# def computepay(money, time):
#     salary = time * money
#     if time > 40:
#         salary = (time - 40) * money * 1.5 + 40 * 10
#     return salary
#     print(salary)
#     print(locals())
#
# computepay(10, 45)


#args, kwargs

# def my_func(*args, **kwargs):
#     if args:
#         print(args)
#     if kwargs:
#         print(kwargs)
# my_func("vdfvrt", 1, 3, 5, name="Nazgul", age=25)

def jf(**kwargs):
    for key, value in kwargs.items():
        locals()[key] = value
    print(locals())
    print(locals()["name"])
jf(name="ns ns", age=15)


+996 707 998 967