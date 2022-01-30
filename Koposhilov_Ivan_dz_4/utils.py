import datetime
import requests
from bs4 import BeautifulSoup


# Для задачи 4_4
def currency_rates(code:str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""

    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    charcodes = soup.find_all('charcode')
    names = soup.find_all('name')
    values = soup.find_all('value')
    data = {}

    for i in range(0, len(charcodes)):
        data[charcodes[i].text] = [names[i].text, values[i].text]
        
    result_value = data.get(code)

    if result_value == None:
        return None
    else:
        return f'{result_value[0]} по отношению к рублю {result_value[1]}'


# Для задачи 4_5
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
    datetime_date = datetime.datetime.strptime(date_value, '%d.%m.%Y').date()
    data = {}

    for i in range(0, len(charcodes)):
        data[charcodes[i].text] = [names[i].text, values[i].text]
        
    kurs = data.get(code)
    if kurs:
        float_kurs = float(kurs[1].replace(',', '.'))
        data_tuple = (float_kurs, datetime_date)
        return data_tuple
    else:
        data_tuple = (kurs, datetime_date)
        return data_tuple


if __name__ == '__main__':
    kurs, date_value = currency_rates_adv("USD")
    empty = bool(not kurs and not date_value)
    if not empty and not isinstance(kurs, float):
        raise TypeError("Неверный тип данных у курса")
    if not empty and not isinstance(date_value, datetime.date):
        raise TypeError("Неверный тип данных у даты")
    print(f'{kurs}, {date_value}')