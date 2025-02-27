# 4) Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в
# порядке их следования в исходном списке. Для выполнения задания обязательно
# использовать генератор.

from random import randint

my_list = [randint(0, 10) for el in range(0, 10)]
print('Исходный список:', my_list)

new_list = [i for i in my_list if my_list.count(i) == 1]
print('Новый список:', new_list)
