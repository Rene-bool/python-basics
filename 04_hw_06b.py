# 6) Реализовать два небольших скрипта:
# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.

from itertools import cycle

print("Скрипт: Бесконечный итератор списка")
for el in cycle("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    print(el)
