# 3) Реализовать программу работы с клетками. Необходимо создать класс Клетка. В его
# конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение ( __add__() ), вычитание ( __sub__() ), умножение ( __mul__() ),
# деление ( __truediv__() ).
# Данные методы должны выполнять увеличение, уменьшение, умножение и обычное (не
# целочисленное) деление клеток, соответственно. В методе деления должно осуществляться
# округление значения до целого числа.
# В классе необходимо реализовать метод make_cell() , принимающий экземпляр класса и
# количество клеток в ряду. Метод должен возвращать строку виду *****\n*****\n***** ..., где
# количество клеток между \n равно переданному аргументу, а количество рядов определяется,
# исходя из общего количества клеток.
# При создании экземпляра клетки должна происходить перезапись параметра, который хранит
# количество клеток.

import math


class Cell:
    def __init__(self, nums):
        self.nums = nums

    def __str__(self):
        return f"Число клеток {self.nums}"

    def __add__(self, other):
        m_sum = self.nums + other.nums
        return Cell(m_sum)

    def __sub__(self, other):
        m_sub = self.nums - other.nums
        return Cell(m_sub)

    def __mul__(self, other):
        m_mul = self.nums * other.nums
        return Cell(m_mul)

    def __truediv__(self, other):
        m_tdiv = math.ceil(self.nums / other.nums)
        return Cell(m_tdiv)

    def make_cell(self, in_row):
        return '\n'.join('*' * in_row for el in range(math.floor(self.nums / in_row))) + '\n' + \
               ('*' * (self.nums % in_row))


nms1 = Cell(21)
nms2 = Cell(6)
print(nms1 + nms2)
print(nms1 - nms2)
print(nms1 * nms2)
print(nms1 / nms2)
print(nms1.make_cell(6))
