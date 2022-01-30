from utils import currency_rates

currencies = ['AUD', 'usd', 'AMD', 'USD', 'EUR', 'KZT', 'CNY']

for currency in currencies:
    print(currency_rates(currency))