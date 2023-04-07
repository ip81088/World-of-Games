import GuessGame
import MemoryGame
import CurrencyRouletteGame

global difficulty, game_choice
from Score import add_score


def welcome(name):
    return 'Hello ' + name + ' and welcome to the World of Games (WoG). Here you can find many cool games to play.'


def load_game():
    print('Please choose a game:')
    print('1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back')
    print('2. Guess Game - guess a number and see if you chose like the computer')
    print('3. Currency Roulette - try and guess the value of a random amount of USD in ILS')

    while True:
        game_choice = int(input('Enter the number of the game you want to play: '))
        if 1 <= game_choice <= 3:
            print('Loading game...')
            break
        else:
            print('Invalid game choice. Please choose a number between 1 and 3.')

    while True:
        difficulty = int(input('Enter the level of difficulty between 1 and 5: '))
        if 1 <= difficulty <= 5:
            print('Starting game...')
            break
        else:
            print('Invalid difficulty. Please choose a number between 1 and 5.')

    if game_choice == 1:
        import MemoryGame
        MemoryGame.play(difficulty)
        if bool(MemoryGame) is True:
            add_score(difficulty=difficulty)
    elif game_choice == 2:
        import GuessGame
        GuessGame.play(difficulty)
        if bool(GuessGame) is True:
            add_score(difficulty=difficulty)
    elif game_choice == 3:
        import CurrencyRouletteGame
        CurrencyRouletteGame.play(difficulty)
        if bool(CurrencyRouletteGame) is True:
            add_score(difficulty=difficulty)
    return difficulty, decision
