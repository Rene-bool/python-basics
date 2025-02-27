# 5) Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title
# (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать
# три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов
# реализовать переопределение метода draw . Для каждого из классов методы должен
# выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет
# описанный метод для каждого экземпляра.


class Stationery:
    title = 'Stationery'

    def draw(self):
        print(f"Запуск отрисовки")


class Pen(Stationery):

    def draw(self):
        print(f"Запуск отрисовки Ручки")


class Pencil(Stationery):

    def draw(self):
        print(f"Запуск отрисовки Карандаша")


class Handle(Stationery):

    def draw(self):
        print(f"Запуск отрисовки Маркера")


p = Pen()
p.draw()

pl = Pencil()
pl.draw()

h = Handle()
h.draw()
