# 6) Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
# Подсказка: использовать функцию count() и cycle() модуля itertools.

from sys import argv
from itertools import count

script_name, start_num = argv

print("Скрипт: Генерация целых чисел начиная с указанного")
for el in count(int(start_num)):
    print(el)
