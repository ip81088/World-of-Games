import requests


def get_money_interval(difficulty):
    url = 'https://v6.exchangerate-api.com/v6/ec62d7fb4e77f9a6b55d9c1a/latest/USD'
    response = requests.get(url)
    data = response.json()
    data['rates']['ILS']


get_money_interval('USD')
print()
