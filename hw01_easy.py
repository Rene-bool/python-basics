__author__ = 'Кутузов Ренат'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.
# код пишем тут...
x = abs(int(input("Enter a number: ")))
i = 10
if x == x % 10:
    print(x)
else:
    while x > 0:
        xi = x % i
        print(xi)
        x = x // i

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!
x = input("Enter variable x: ")
y = input("Enter variable y: ")
print("Initial x = ", x,"\nInitial y = ", y)
z = x
x = y
y = z
print("Final x = ",x,"\nFinal y = ",y)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"
x = int(input("Укажите ваш возраст, лет: "))
if x >= 18:
    print("Доступ разрешен")
else:
    print("Извините, пользование данным ресурсом только с 18 лет")
