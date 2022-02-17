


class TrafficLight:
    """Атрибут класса светофор"""
    __color: dict = {'red': 4, 'yellow': 2, 'green': 3}

    def running(self):
        """Переключение между режимами"""
        for k, v in self.__color.items():
            print(f'{k} {v} сек')



if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()
    traffic.__color = 'blue'
    print((traffic.__color, TrafficLight.__color))