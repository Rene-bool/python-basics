# 1) Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод
# running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
# переключение светофора в режимы: красный, желтый, зеленый. Время перехода между
# режимами должно составлять 7 и 2 секунды. Проверить работу примера, создав экземпляр и
# вызвав описанный метод.

import time


class TrafficLight:
    # __color = 'color'

    def t_running(self):
        i = 7
        j = 2
        self.__color = 'Red'
        print(self.__color)
        time.sleep(i)  # in seconds
        self.__color = 'Yellow'
        print(self.__color)
        time.sleep(j)  # in seconds
        self.__color = 'Green'
        print(self.__color)


t = TrafficLight()
t.t_running()
