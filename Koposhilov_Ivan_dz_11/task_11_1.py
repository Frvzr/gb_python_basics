import datetime


class Date:

    @classmethod
    def get_date(cls, date):
        """
        Извлекает число, месяц, год и преобразовыват их тип к типу Число
        """
        cls.validate_data(date)
        date = date.split('-')
        return f'день: {int(date[0])}\nмесяц: {int(date[1])}\nгод: {int(date[2])}'

    @staticmethod
    def validate_data(date):
        """
        Валидация даты
        """
        try:
            datetime.datetime.strptime(date, '%d-%m-%Y')
            return f'{date}: Корректная дата'
        except ValueError:
            raise ValueError('Некоректная дата')


if __name__ == '__main__':
    date = Date()
    print(Date.get_date('11-12-2020'))
    print(date.validate_data('20-02-2021'))
    try:
        print(date.validate_data('32-12-2021'))
    except ValueError as err:
        print(err)  