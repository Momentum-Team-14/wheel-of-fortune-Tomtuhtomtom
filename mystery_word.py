import random
import os


def play_game():
    cls()
    print('Welcome to Mystery Word!!')
    read_the_rules()
    ask_to_play()
    with open('words.txt', 'r') as words_file:
        solution_word = select_random_word(words_file)
    len_of_answer = number_of_letters(solution_word)
    show_partial_answer(len_of_answer)
    all_choices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
               'W', 'X', 'Y', 'Z']
    check_letter(all_choices)


# clears the console
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# ask the user to play
def ask_to_play():
    play = input('Would you like to play? [Y/N] ').upper()
    if play != 'Y' and play != 'N':
        print("Invalid Entry")
        ask_to_play()
    else:
        if play == 'Y':
            return
        else:
            exit()


# ask the user if they want to read the rules
def read_the_rules():
    rules = input('Would you like to read the rules? [Y/N] ').upper()
    if rules != 'Y' and rules != 'N':
        print("Invalid Entry")
        read_the_rules()
    else:
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
    print(f'The Mystery Word has {len(answer)} letters!')
    return len(answer)


# displays partial answer
def show_partial_answer(answer):
    blanks = answer * " __ "
    print(f'\n " {blanks} "\n')


# check for guessed letter
def check_letter(choices_left):
    print(f'Choices available:\n{" ".join(choices_left)}\n')
    user_letter = input('Pick a letter: ').upper()
    print(user_letter)


if __name__ == "__main__":
    play_game()
