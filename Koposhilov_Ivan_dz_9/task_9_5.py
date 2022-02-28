

class Stationery:
    def __init__(self, title: str) -> None:
        """конструктор класса
        :param title: канцелярская принадлежность
        """
        self.title = title

    def draw(self) -> None:
        """Запуск отрисовки"""
        return 'Запуск отрисовки'



# определите классы ниже согласно условий задания
class Pen(Stationery):
    def draw(self):
        """Переопределяет отрисовку"""
        print(super().draw())
        return f'{self.__class__.__name__}: приступил к отрисовке объекта "{self.title}"'



class Pencil(Stationery):
    def draw(self):
        """Переопределяет отрисовку"""
        print(super().draw())
        return f'{self.__class__.__name__}: приступил к отрисовке объекта "{self.title}"'



class Handle(Stationery):
    def draw(self):
        """Переопределяет отрисовку"""
        print(super().draw())
        return f'{self.__class__.__name__}: приступил к отрисовке объекта "{self.title}"'



if __name__ == '__main__':
    pen = Pen('Ручка')
    pencil = Pencil('Карандаш')
    handle = Handle('Маркер')
    print(pen.draw())  # Pen: приступил к отрисовке объекта "Ручка"
    print(handle.draw())  # Handle: приступил к отрисовке объекта "Маркер"
    print(pencil.draw())  # Пример вывода ниже в многострочном комментарии
    """
    Запуск отрисовки
    Pencil: приступил к отрисовке объекта "Карандаш"
    """