# 2) Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
# сущность (класс) этого проекта — одежда , которая может иметь определенное название. К
# типам одежды в этом проекте относятся пальто и костюм . У этих типов одежды существуют
# параметры: размер (для пальто ) и рост (для костюма ). Это могут быть обычные числа: V и
# H , соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5) , для костюма (2*H + 0.3) . Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
# знания: реализовать абстрактные классы для основных классов проекта, проверить на
# практике работу декоратора @property .

# С ПОМОЩЬЮ НАСТАВНИКА

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name


class Coat(Clothes):
    def __init__(self, name, V):
        super().__init__(name)
        self.V = V

    @property
    def mat_calc(self):
        return f'Для пошива изделия {self.name} потребуется %.1f ед. материала' % (self.V / 6.5 + 0.5)


class Suit(Clothes):
    def __init__(self, name, H):
        super().__init__(name)
        self.H = H

    @property
    def mat_calc(self):
        return f'Для пошива изделия {self.name} потребуется %.1f ед. материала' % (2 * self.H + 0.3)


mat_coat = Coat('Пальто', 150)
print(mat_coat.mat_calc)

mat_suit = Suit('Костюм', 15)
print(mat_suit.mat_calc)
