import requests
from bs4 import BeautifulSoup


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
        return f'Курс валюты {result_value[0]} по отношению к рублю {result_value[1]}р.'


if __name__ == '__main__':
    print(currency_rates("USD"))
    print(currency_rates("noname"))