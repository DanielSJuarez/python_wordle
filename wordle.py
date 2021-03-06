import urllib.request
import random

alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
               
guess_display = ''


class color:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    WHITE = '\033[97m'
    RED = '\033[91m'


URL = 'https://gist.githubusercontent.com/cfreshman/a03ef2cba789d8cf00c08f767e0fad7b/raw/5d752e5f0702da315298a6bb5a771586d6ff445c/wordle-answers-alphabetical.txt'

with urllib.request.urlopen(URL) as response:
    word_list = response.read().splitlines()


def win(user_guess, wordle_word):
    '''
    user_guess and wordle_word are strings of the guessed word and answer
    returns if the user guess matched the correct word
    '''

    if user_guess == wordle_word:
        return True
    return False


def update_available_alphabet(color_letter, value):

    '''
    color_letter: is the new color of the alphabet letter depending on the user guess
    value is the letter being tested
    updates the color values of the alphabet to show the user their guessed letters
    '''

    global alphabet_list
    source_alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 

    # if value not in alphabet_list:
    #     return
    # else:
    new_index = source_alphabet_list.index(value)
    alphabet_list.pop(new_index)
    alphabet_list.insert(new_index, color_letter)


def display_user_guess(user_guess, wordle_word):

    '''
    wordle_word_list is a list of the answer
    user_guess is a string of the current guessed submission by the user
    returns an updated display of the user guess that is color sorted depending on correct value and index
    '''

    global guess_display
    wordle_word_list = list(wordle_word)
    color_letter = ''

    for index, value in enumerate(user_guess):
        if value == wordle_word_list[index]:
            color_letter = f"{color.GREEN}{value}{color.WHITE}"
            guess_display += color_letter
            update_available_alphabet(color_letter, value)
        elif value in wordle_word:
            color_letter = f"{color.YELLOW}{value}{color.WHITE}"
            guess_display += color_letter
            update_available_alphabet(color_letter, value)
        else:
            guess_display += value
            color_letter = f"{color.RED}{value}{color.WHITE}"
            update_available_alphabet(color_letter, value)
    guess_display += '\n'
    return guess_display


def wordle(wordle_word):

    '''
    wordle_word is a string word that is always 5 letters long that the user is trying to guess
    returns the user input, displays the guess attempts, calls all user visiual displays, and the win/loss statements
    '''

    guess_attempts = 6
    print('Welcome to Wordle')
    print('Please enter a five lettter word! Guess correct letter, correct spot! = Green')
    print('Guess correct letter, wrong spot! = Yellow')
    print('Guess the wrong letter! = Red.')
    print('You have', guess_attempts, 'guesses. Good Luck!!!')

    while guess_attempts > 0:
        user_guess = input('Enter a five letter word ').upper()
        if len(user_guess) != 5: 
            print('That was not a 5 letter word, please enter a five letter word!')
        elif user_guess.isalpha() != True:
            print('You have not entered all letter, please enter a five letter word!')
        else:
            print(display_user_guess(user_guess, wordle_word))
            if win(user_guess, wordle_word) == True:
                guess_attempts -= 1
                print('Congratulations!! You have guessed ', wordle_word,
                    'it took you', (6 - guess_attempts), 'guesses')
                break
            else:
                print(''.join(alphabet_list))
                guess_attempts -= 1
                print('You have', guess_attempts,'guesses left!')
                if guess_attempts < 1:
                    print('Sorry, You ran out of guesses. The word was ', wordle_word)
                    break


wordle_word = random.choice(word_list).decode('utf-8').upper()
wordle(wordle_word)
