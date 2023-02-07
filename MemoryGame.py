import time
import os


def generate_sequence(difficulty):
    import random
    random_numbers = []
    for number in range(difficulty):
        random_numbers.append(int(random.uniform(1, 101)))
    print(random_numbers)
    time.sleep(0.7)
    os.system('cls' if os.name == 'nt' else 'clear')
    return random_numbers


def get_list_from_user(difficulty):
    user_numbers = []
    print(f'Please enter {difficulty} numbers')
    for number in range(difficulty):
        user_numbers.append(int(input(f'What is the [{number+1}] Number: ')))
    return user_numbers


def is_list_equal(random_numbers, user_numbers):
    random_numbers()
    user_numbers.sort()
    os.system('cls' if os.name == 'nt' else 'clear')
    if random_numbers == user_numbers:
        return True
    else:
        return False


def play(difficulty):
    random_numbers = generate_sequence(difficulty)
    user_numbers = get_list_from_user(difficulty)
    if is_list_equal(random_numbers, user_numbers):
        print('True')
    else:
        print('False')
