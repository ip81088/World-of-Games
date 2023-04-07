import random
import os
import requests


def get_money_interval(difficulty):
    url = 'https://v6.exchangerate-api.com/v6/ec62d7fb4e77f9a6b55d9c1a/latest/USD'
    response = requests.get(url)
    data = response.json()
    exchange = data['conversion_rates']["ILS"]
    usd = int(random.uniform(1, 100))
    t = usd * exchange
    low = int(t - (5 - difficulty))
    high = int(t + (5 - difficulty))
    return usd, t, low, high


def get_guess_from_user(usd):
    while True:
        try:
            guess = int(input(f"Guess the value of {usd}$ in ILS: "))
        except ValueError:
            print("Error: Enter just numbers please, not letters, words ,etc...")
            continue
        return guess


def play(difficulty):
    usd, t, low, high = get_money_interval(difficulty)
    guess = get_guess_from_user(usd)
    os.system('cls' if os.name == 'nt' else 'clear')
    if high >= guess >= low:
        return True
    else:
        return False
