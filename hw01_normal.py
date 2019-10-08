__author__ = 'Кутузов Ренат'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.
x = abs(int(input("Enter a number: ")))
i = 10
x0 = 0
if x < 10:
    print("Заданное число состоит из одной цифры")
else:
    while x > 0:
        x1 = x % i
        a = [x0, x1]
        x1 = max(a)
        x = x // i
        if x == 0:
            break
        else:
            x0 = x % i
            a = [x0, x1]
            x0 = max(a)
            x = x // i
    print("Максимальная цифра в заданном числе:", max(a))

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.
x = int(input("Enter variable x: "))
y = int(input("Enter variable y: "))
print('Initial x =', x, '\n'
                        'Initial y =', y)
x = x + y
y = x - y
x = x - y
print('Final x =', x, '\n'
                      'Final y =', y)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4
import math
a = float(input('Enter coefficient "a" for equation ax² + bx + c: '))
b = float(input('Enter coefficient "b" for equation ax² + bx + c: '))
c = float(input('Enter coefficient "c" for equation ax² + bx + c: '))
if a == 0:
    x = -c / b
    print('The root of the equation is x =', x)
else:
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print('The first root of the equation is x1 =', x1, '\n'
                                                            'The second root of the equation is x2 =', x2)
    if d == 0:
        x = -b / (2 * a)
        print('The root of the equation is x =', x)
    if d < 0:
        print('The equation has no real roots')
