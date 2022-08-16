import random
import os

ALL_CHOICES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
               'W', 'X', 'Y', 'Z']


def play_game():
    cls()
    print('Welcome to Mystery Word!!')
    read_the_rules()
    ask_to_play()
    with open('words.txt', 'r') as words_file:
        solution_word = select_random_word(words_file)
    len_of_answer = number_of_letters(solution_word)
    blank_answer = show_blank_answer(len_of_answer)
    guesses_total = 8
    # check_letter_availability(ALL_CHOICES, guesses_total)  # put line in guess()
    guess_the_letter(blank_answer, solution_word, guesses_total)


# clears the console
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


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


# ask the user to play
def ask_to_play():
    play = input('Would you like to play? [Y/N] ').upper()
    if play != 'Y' and play != 'N':
        print("Invalid Entry")
        ask_to_play()
    else:
        if play == 'Y':
            cls()
        else:
            exit()


# uses txt file to select a random word
def select_random_word(file):
    list_of_words = file.read().replace('\n', ' ').split()
    return random.choice(list_of_words)


# tells user how many letters in the word
def number_of_letters(answer):
    print(f'The Mystery Word has {len(answer)} letters!')
    return len(answer)


# displays partial answer
def show_blank_answer(answer):
    blanks = answer * [" __ "]
    print(f'\n"{" ".join(blanks)}"\n')
    return blanks


# check for guessed letter
def check_letter_availability(choices_left, guess):
    print(f'Choices available:\n{" ".join(choices_left)}')
    if guess in choices_left and len(guess) == 1:
        for i in range(len(choices_left)):
            if choices_left[i] == guess:
                choices_left[i] = ' '
                # return guess  # may need this
    elif len(guess) > 1:
        print("Invalid Entry, try again")
        guess = input('Pick a letter: ').upper()
        check_letter_availability(choices_left, guess)
    else:
        print(f"You've picked {guess} already, try again")
        guess = input('Pick a letter: ').upper()
        check_letter_availability(choices_left, guess)
    # return choices_left  # may not need, never gets to here


# check if guessed letter is right or wrong
def guess_the_letter(partial_answer, answer, guesses):
    answer_key = list(answer)
    user_guess = input('Pick a letter: ').upper()
    if user_guess in answer_key:
        for i in range(len(answer_key)):
            if user_guess == answer_key[i]:
                partial_answer[i] = answer_key[i]
        print(partial_answer)
        if " __ " not in partial_answer:
            cls()
            print("You guessed all the letters!!!")
            print(f'The Mystery Word was: \n{"".join(partial_answer)}\n')
            print("YOU WON!    " * 50)
            try_again()
        if guesses > 0:
            guess_the_letter(partial_answer, answer, guesses)
    else:
        guesses -= 1
        if guesses > 0:
            guess_the_letter(partial_answer, answer, guesses)
        else:
            cls()
            print(f'You are out of guesses\nThe Mystery Word was: \n{answer}\n')
            print("GAME OVER")
            try_again()


def try_again():
    again = input('Would you like to play again? [Y/N] ').upper()
    if again != 'Y' and again != 'N':
        print("Invalid Entry")
        try_again()
    else:
        if again == 'Y':
            play_game()
        else:
            exit()


if __name__ == "__main__":
    play_game()
