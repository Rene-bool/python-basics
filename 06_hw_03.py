# 3) Реализовать базовый класс Worker (работник), в котором определить атрибуты: name ,
# surname , position (должность), income (доход). Последний атрибут должен быть
# защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"profit": profit, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker .
# В классе Position реализовать методы получения полного имени сотрудника ( get_full_name ) и
# дохода с учетом премии ( get_full_profit) . Проверить работу примера на реальных данных
# (создать экземпляры класса Position , передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).


class Worker:
    def __init__(self, name, surname, position, profit, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"profit": profit, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, profit, bonus):
        super().__init__(name, surname, position, profit, bonus)

    def get_full_name(self, name, surname):
        self.name = name
        self.surname = surname

    def get_full_profit(self, _income):
        pass
        # self.profit = profit
        # self.bonus = bonus
        self._income = _income


n = Position('Ivan', 'Novak', 'CEO', 10000, 3000)
print(n.name + ' ' + n.surname)
print(n._income)
