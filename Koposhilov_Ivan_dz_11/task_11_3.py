class Error(Exception):
    
    def __init__(self):
        """
        Определяем пустой словарь для хранения чисел
        """
        self.list_number = []

    def create_list(self):
        """
        Запрашиваем числа у пользователя, слово для остановки стоп
        """
        while True:
            user_answer = input('Введите число и нажимайте Enter или stop - чтобы закончить: ')
            try:
                user_answer.isnumeric()
                self.list_number.append(int(user_answer))
                print(f'Текущий список - {self.list_number}')
            except:
                if user_answer.lower() == 'stop' or user_answer.lower() == 'стоп' or user_answer.lower() == 'ыещз':
                    break
                else:
                    print(f"Недопустимое значение")

        return f'Вы вышли, итоговый список - {self.list_number}'       

list_error = Error()
print(list_error.create_list())