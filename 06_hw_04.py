# 4) Опишите несколько классов: TownCar , SportCar , WorkCar , PoliceCar . У каждого класса
# должны быть следующие атрибуты: speed , color , name , is_police (булево). А также несколько
# методов: go , stop , turn(direction) , которые должны сообщать, что машина поехала,
# остановилась, повернула (куда).


class TownCar:
    speed = 60
    color = 'Yellow'
    name = 'Cabby'
    is_police = False

    def go(self):
        print(f"Автомобиль {self.name} начал движение")

    def stop(self):
        print(f"Автомобиль {self.name} остановился")

    def turn(self, turn_angle):
        self.turn_angle = turn_angle
        if self.turn_angle > 0:
            print(f"Автомобиль {self.name} повернул налево")
        elif self.turn_angle < 0:
            print(f"Автомобиль {self.name} повернул направо")
        else:
            print(f"Автомобиль {self.name} движется прямо")


class SportCar:
    speed = 380
    color = 'Red'
    name = 'Sport Car'
    is_police = False

    def go(self):
        print(f"Автомобиль {self.name} начал движение")

    def stop(self):
        print(f"Автомобиль {self.name} остановился")

    def turn(self, turn_angle):
        self.turn_angle = turn_angle
        if self.turn_angle > 0:
            print(f"Автомобиль {self.name} повернул налево")
        elif self.turn_angle < 0:
            print(f"Автомобиль {self.name} повернул направо")
        else:
            print(f"Автомобиль {self.name} движется прямо")


class WorkCar:
    speed = 40
    color = 'Grey'
    name = 'Worker'
    is_police = False

    def go(self):
        print(f"Автомобиль {self.name} начал движение")

    def stop(self):
        print(f"Автомобиль {self.name} остановился")

    def turn(self, turn_angle):
        self.turn_angle = turn_angle
        if self.turn_angle > 0:
            print(f"Автомобиль {self.name} повернул налево")
        elif self.turn_angle < 0:
            print(f"Автомобиль {self.name} повернул направо")
        else:
            print(f"Автомобиль {self.name} движется прямо")


class PoliceCar:
    speed = 180
    color = 'Black'
    name = 'Officer'
    is_police = True

    def go(self):
        print(f"Автомобиль {self.name} начал движение")

    def stop(self):
        print(f"Автомобиль {self.name} остановился")

    def turn(self, turn_angle):
        self.turn_angle = turn_angle
        if self.turn_angle > 0:
            print(f"Автомобиль {self.name} повернул налево")
        elif self.turn_angle < 0:
            print(f"Автомобиль {self.name} повернул направо")
        else:
            print(f"Автомобиль {self.name} движется прямо")


t = TownCar()
t.go()
t.turn(10)
t.turn(-10)
t.stop()

s = SportCar()
s.go()
s.turn(10)
s.turn(-10)
s.stop()

w = WorkCar()
w.go()
w.turn(10)
w.turn(-10)
w.stop()

p = PoliceCar()
p.go()
p.turn(10)
p.turn(-10)
p.stop()
