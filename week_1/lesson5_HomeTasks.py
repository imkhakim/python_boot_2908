#Task1

temperature = float(input("Введите температуру в градусах Цельсия:"))

if temperature < -273.15:
    print("Температура недействительна, потому что она ниже абсолютного нуля!")
elif temperature == -273.15:
    print("Температура равна абсолютному нулю!")
elif temperature < 0:
    print("Температура ниже точки замерзания!")
elif temperature == 0:
    print("Температура находится в точке замерзания!")
elif temperature < 100:
    print("Температура находится в нормальном диапазоне!")
elif temperature == 100:
    print("Температура находится в точке кипения!")
elif temperature > 100:
    print("Температура выше точки кипения!")

#Task2

year = int(input("Введите год:"))

if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
    print("NO")
else:
    print("YES")


#Task3

amount = int(input("Введите требуемое количество товара:"))

if amount < 0:
    print("Введите положительное число!")
elif amount < 11:
    print(amount * 12)
elif amount < 100:
    print(amount * 10)
else:
    print(amount * 7)

