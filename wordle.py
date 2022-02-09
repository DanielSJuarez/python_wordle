import urllib.request
import random

alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


class color:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    WHITE = '\033[97m'


URL = 'https://gist.githubusercontent.com/cfreshman/a03ef2cba789d8cf00c08f767e0fad7b/raw/5d752e5f0702da315298a6bb5a771586d6ff445c/wordle-answers-alphabetical.txt'

with urllib.request.urlopen(URL) as response:
    word_list = response.read().splitlines()


def win(user_guess, wordle_word):
    if user_guess == wordle_word:
        return True
    return False


def update_available_alphabet(value):
    global alphabet_list
    alphabet_list.pop(alphabet_list.index(value))


def display_user_guess(user_guess, wordle_word):
    guess_display = ''
    wordle_word_list = list(wordle_word)

    for index, value in enumerate(user_guess):
        if value == wordle_word_list[index]:
            correct_placement_letter = f'{color.GREEN} {value} {color.WHITE}'
            guess_display += correct_placement_letter
        elif value in wordle_word:
            incorrect_placement_letter = f"{color.YELLOW} {value} {color.WHITE}"
            guess_display += incorrect_placement_letter
        else:
            guess_display += value
            update_available_alphabet(value)
    guess_display += '\n'
    return guess_display


def wordle(wordle_word):

    guess_attempts = 6
    print(wordle_word)
    print('Welcome to Wordle')
    print('Please enter a five lettter word, letters that are right and in the correct spot will be colored green, right letters but in the incorrect spot will be yellow. Otherwise they will be not be made available to guess again. Good luck')

    while guess_attempts > 0:
        print('You have', guess_attempts, 'remaining')
        user_guess = input('Enter a five letter word ').upper()
        print(display_user_guess(user_guess, wordle_word))
        if win(user_guess, wordle_word) == True:
            print('Congratulation!! You have guessed', wordle_word, 'it took you', (6 - guess_attempts), 'guesses')
        print(alphabet_list)
        guess_attempts -= 1


wordle_word = random.choice(word_list).decode('utf-8').upper()
wordle(wordle_word)

print('Sorry, You ran out of guesses. The word was', wordle_word)
