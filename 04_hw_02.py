# 2) Представлен список чисел. Необходимо вывести элементы исходного списка, значения
# которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для
# формирования списка использовать генератор.

from random import randint

my_list = [randint(0, 10) for el in range(0, 10)]
print('Исходный список:', my_list)

i = 0
new_list = []

while i + 1 < len(my_list):
    i += 1
    if my_list[i] > my_list[i - 1]:
        new_list.append(my_list[i])
print('Новый список:', new_list)

# не разобрался как сформировать новый список с помощью генератора
