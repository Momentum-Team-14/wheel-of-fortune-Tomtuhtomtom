import random
import os


def play_game():
    cls()
    print('Welcome to Mystery Word!!')
    read_the_rules()
    ask_to_play()
    with open('test-word.txt', 'r') as words_file:
        solution_word = select_random_word(words_file)
    print(solution_word)
    number_of_letters(solution_word)


# clears the console
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# ask the user to play
def ask_to_play():
    play = input('Would you like to play? [Y/N] ').upper()
    if play == 'Y':
        return
    else:
        exit()


# ask the user if they want to read the rules
# need to write rules file
def read_the_rules():
    rules = input('Would you like to read the rules? [Y/N] ').upper()
    if rules == 'Y':
        with open('rules.txt', 'r') as rules_file:
            rules_txt = rules_file.read()
            print(rules_txt)
            return
    else:
        return


# uses txt file to select a random word
def select_random_word(file):
    list_of_words = file.read().replace('\n', ' ').split()
    return random.choice(list_of_words)


# tells user how many letters in the word
def number_of_letters(answer):
    pass
    print(f'The Mystery Word has {len(answer)} letters!')


# displays partial answer
def show_partial_answer():
    pass


if __name__ == "__main__":
    play_game()
