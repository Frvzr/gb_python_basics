from turtle import speed



class Car:
    is_police: bool = False

    def __init__(self, speed: int, color: str, name: str):
        """
        Конструктор класса
        :param speed: текущая скорость автомобиля
        :param color: цвет автомобиля
        :param name: название марки автомобиля
        """
        self.speed = speed
        self.color = color
        self.name = name

    def go(self) -> None:
        """
        Увеличивает значение скорости на 15
        :return: в stdout сообщение по формату
            'Машина <название марки машины> повысила скорость на 15: <текущая скорость машины>'
        """
        self.speed += 15
        return f'{self.name} повысила скорость на 15: {self.speed}'

    def stop(self) -> None:
        """
        При вызове метода скорость становится равной '0'
        :return: в stdout сообщение по формату '<название марки машины>: остановилась'
        """
        self.speed = 0
        return f'{self.name}: остановилась'

    def turn(self, direction: str) -> None:
        """
        Принимает направление движения автомобиля
        :param direction: строковое представление направления движения, может принимать только
            следующие значения: 'направо', 'налево', 'прямо', 'назад'
        :return: в stdout сообщение по формату
            '<название марки машины>: движется <direction>'
        """
        directions = ['направо', 'налево', 'прямо', 'назад']
        #direction = direction 
        if direction not in directions:
            raise ValueError('нераспознанное направление движения')
        else:
            return f'{self.name}({self.__class__.__name__}): движется {direction}'

    def show_speed(self) -> None:
        """
        Проверка текущей скорости автомобиля
        :return: в stdout выводит сообщение формата
            '<название марки машины>: текущая скорость <значение текущей скорости> км/час'
        """
        if self.is_police == False:
            return f'{self.name}: текущая скорость {self.speed} км/час'
        else:

            return f'{self.name}: текущая скорость {self.speed} км/час\nВруби мигалку и забудь про скорость!'



# определите классы TownCar, WorkCar, SportCar, PoliceCar согласно условия задания
class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return 'Alarm!!! Speed!!!'
        else:
            return f'{self.name}: текущая скорость {self.speed} км/час'



class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return 'Alarm!!! Speed!!!'
        else:
            super().show_speed()
            #return f'{self.name}: текущая скорость {self.speed} км/час'



class PoliceCar(Car):
    def show_speed(self):
        if self.speed > 100:
            self.is_police = True
            return super().show_speed()



class SportCar(Car):
    pass



if __name__ == '__main__':
    town_car = TownCar(41, "red", 'WW_Golf')
    work_car = WorkCar(41, 'yellow', 'BobCat')
    police_car = PoliceCar(120, "blue", 'BMW')
    sport_car = SportCar(300, 'white', 'Ferrari')
    print(town_car.go())  # Машина WW_Golf повысила скорость на 15: 56
    print(town_car.show_speed())  # WW_Golf: текущая скорость 56 км/час
    print(work_car.show_speed())  # Alarm!!! Speed!!!
    print(town_car.stop())  # WW_Golf: остановилась
    print(police_car.show_speed())
    # BMW: текущая скорость 120 км/час
    # Вруби мигалку и забудь про скорость!
    print(sport_car.turn('назад'))  # Ferrari(SportCar): движется назад
    print(sport_car.turn('right'))
    """
    Traceback (most recent call last):
      ...
    ValueError: нераспознанное направление движения
    """
    # print(town_car.go())
    # print(town_car.show_speed())