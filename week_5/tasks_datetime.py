#task1, 2

'''Попросите пользователя ввести год, а затем используйте модуль datetime, чтобы проверить,
является ли этот год високосным, и выведите результат.

Попросите пользователя ввести две даты (начальную и конечную), а затем используйте модуль datetime
для подсчета количества рабочих дней между этими датами, исключая выходные дни.'''

#task1

# сделал через calendar так как для datetime нет метода isleap()

import datetime

import calendar

year = int(input("Enter year: "))

is_leap = calendar.isleap(year)

if is_leap:
    print(str(year) + " is leap year")
else:
    print(str(year) + " is not leap year")


#task2

def get_days(start_date, end_date):

    start_date = (datetime.datetime.strptime(start_date, "%Y-%m-%d")).date()
    end_date = (datetime.datetime.strptime(end_date, "%Y-%m-%d")).date()

    all_days = ((end_date - start_date).days + 1)
    print("Общее количество дней в заданном периоде: " + str(all_days))

    days_in_period = (start_date + datetime.timedelta(x) for x in range((end_date - start_date).days + 1))
    work_days = sum(1 for day in days_in_period if day.weekday() < 5)

    print("Количество рабочих дней в заданном периоде: " + str(work_days))

get_days(input('Введите начальную дату в формате "XXXX-XX-XX" (год-месяц-день): '),
         input('Введите конечную дату в формате "XXXX-XX-XX" (год-месяц-день): '))

