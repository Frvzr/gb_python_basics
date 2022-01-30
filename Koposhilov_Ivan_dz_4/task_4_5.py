from utils import currency_rates_adv
import sys
import datetime

try:
    currency = sys.argv[1]
except IndexError:
    print('Необходимо ввести валюту')
else:
    kurs, date_value = currency_rates_adv(currency)   
    empty = bool(not kurs and not date_value)
    if not empty and not isinstance(kurs, float):
        raise TypeError("Неверный тип данных у курса")
    if not empty and not isinstance(date_value, datetime.date):
        raise TypeError("Неверный тип данных у даты")
    print(f'{kurs}, {date_value}')
