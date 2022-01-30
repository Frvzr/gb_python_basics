import datetime
import requests
from bs4 import BeautifulSoup


def currency_rates_adv(code: str):
    """возвращает курс валюты `code` по отношению к рублю"""

    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    charcodes = soup.find_all('charcode')
    names = soup.find_all('name')
    values = soup.find_all('value')
    tag = soup.valcurs
    date_value = tag['date']
    datetime_date = datetime.datetime.strptime(date_value, '%d.%m.%Y')
    data = {}

    for i in range(0, len(charcodes)):
        data[charcodes[i].text] = [names[i].text, values[i].text]
        
    kurs = data.get(code)
    float_kurs = float(kurs[1].replace(',', '.'))
    data_tuple = (float_kurs, datetime_date)
    return data_tuple

kurs, date_value = currency_rates_adv("USD")
empty = bool(not kurs and not date_value)
if not empty and not isinstance(kurs, float):
    raise TypeError("Неверный тип данных у курса")
if not empty and not isinstance(date_value, datetime.date):
    raise TypeError("Неверный тип данных у даты")
print(kurs, date_value)