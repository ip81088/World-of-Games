from time import sleep


def generate_number(difficulty):
    import random
    secret_number = int(random.randint(1, difficulty))
    return secret_number


def get_guess_from_user(difficulty):
    number = int((input(f'Choose a number between 1 and {difficulty}: ')))
    return number


def compare_results(secret_number, number):
    if secret_number == number:
        return True
    else:
        return False


def play(difficulty):
    secret_number = generate_number
    print('Generating number...')
    sleep(0.7)
    number = get_guess_from_user(difficulty)
    if compare_results(secret_number=secret_number, number=number):
        print('True')
    else:
        print('False')
