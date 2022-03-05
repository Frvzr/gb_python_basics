class WarehouseOfficeEquipment:

    def __init__(self):
        """
        Определяем словарь для хранения данных
        """
        self.warehouse = {}

    def add_equipment(self, equipment, quantity):
        """
        Функция для добавления офисного оборудования
        equipment: класс оборудования, по нему распознается имя и модель принимаемого оборудования
        quantity: количество добавляемого оборудования
        return: выводится словарь с добавленным оборудованием
        """
        self.check_attr(quantity)
        equipment_type = equipment.get_name_class()
        equipment_model = equipment.name
        if equipment_type in self.warehouse and equipment_model in self.warehouse[equipment_type]:
            store_qty = self.warehouse[equipment_type][equipment_model]
            total_qty = store_qty + quantity
            self.warehouse[equipment_type][equipment_model] = total_qty
        elif equipment_type in self.warehouse and equipment_model not in self.warehouse[equipment_type]:
            self.warehouse[equipment_type][equipment_model] = quantity
        else:
            self.warehouse[equipment_type] = {}
            self.warehouse[equipment_type][equipment_model] = quantity
        return self.warehouse

    def get_equipment(self, equipment, model, quantity):
        """
        Функция для удаления офисного оборудования
        equipment: название извлекаемого оборудования
        model: модель оборудования
        quantity: количество извлекаемого оборудования
        return: выводится итоговый словарь оборудованием
        """
        self.check_attr(quantity)
        if equipment in self.warehouse:
            if model in self.warehouse[equipment]:
                store_qty = self.warehouse[equipment][model]
                if store_qty >= quantity:
                    total_qty = store_qty - quantity
                    self.warehouse[equipment][model] = total_qty
                else:
                    return "Ошибка: запрашиваемое количество больше чем на складе"
            else:
                return 'Ошибка: на складе нет данной модели'
        else:
            return 'Ошибка: на складе нет такого оборудования'
        return self.warehouse

    def check_attr(self, qty):
        """
        Функция для проверки правильности ввода количества оборудования
        """
        if type(qty) != int:
            raise TypeError('Неправильный ввод данных, введите целое число')


class OfficeEquipment(WarehouseOfficeEquipment):
    def __init__(self, model):
        self.name = model
        self.class_name = self.__class__.__name__

    def get_name_class(self):
        """
        Функция для извлечение текущего названия класса которы впоследствии передается ключом в словарь
        """
        return f'{self.class_name}'

class Printer(OfficeEquipment):
    def __init__(self, model):
        super().__init__(model)


class Scanner(OfficeEquipment):
    def __init__(self, model):
        super().__init__(model)


class Copier(OfficeEquipment):
    def __init__(self, model):
        super().__init__(model)
    
if __name__ == '__main__':
    store = WarehouseOfficeEquipment()
    prnt = Printer('Epson')
    store.add_equipment(prnt, 3)
    prnt_2 = Printer('HP')
    store.add_equipment(prnt_2, 8)
    prnt_3 = Printer('HP')
    store.add_equipment(prnt_2, 8)
    scn = Scanner('Epson')
    store.add_equipment(scn, 8)
    cpr = Copier('Xerox')
    store.add_equipment(cpr, 17)
    print(store.warehouse)
    print(store.get_equipment('Printer', 'HP', 5))
    print(store.get_equipment('Pinter', 'Epson', 1))
    print(store.get_equipment('Printer', 'Erson', 1))
    print(store.get_equipment('Printer','Epson', 500))
