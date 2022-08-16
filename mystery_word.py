import random
import os

ALL_LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
               'W', 'X', 'Y', 'Z']

initial_list_for_letters = []


def play_game(choice_letters):
    cls()
    print(f'{"***Welcome to Mystery Word!!***"}\n')
    read_the_rules()
    ask_to_play()
    choice_letters = ALL_LETTERS[:]
    with open('words.txt', 'r') as words_file:
        # solution_word = select_random_word(words_file)
        # use above line if you don't want difficulty setting and omit line below
        solution_word = choose_your_difficulty(words_file)
    # print(solution_word)  Answer if need to see for testing
    len_of_answer = number_of_letters(solution_word)
    blank_answer = show_blank_answer(len_of_answer)
    answer_key = list(solution_word)
    guesses_total = 8
    guess_the_letter(blank_answer, answer_key, guesses_total, choice_letters)


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
        if play == 'N':
            exit()
        else:
            return


# Choose difficulty
def choose_your_difficulty(file):
    list_of_words = file.read().replace('\n', ' ').upper().split()
    easy_words = [word for word in list_of_words if len(word) >= 4 and len(word) <= 6]
    normal_words = [word for word in list_of_words if len(word) >= 6 and len(word) <= 8]
    hard_words = [word for word in list_of_words if len(word) >= 8]
    diff_setting = input('Choose your difficulty: [E]asy, [N]ormal, or [H]ard ').upper()
    if diff_setting == 'E' or diff_setting == 'EASY':
        solution = random.choice(easy_words)
        cls()
        return solution
    elif diff_setting == 'N' or diff_setting == 'NORMAL':
        solution = random.choice(normal_words)
        cls()
        return solution
    elif diff_setting == 'H' or diff_setting == 'HARD':
        solution = random.choice(hard_words)
        cls()
        return solution
    else:
        print("Invalid Entry")
        choose_your_difficulty(file)


# uses txt file to select a random word
def select_random_word(file):
    list_of_words = file.read().replace('\n', ' ').upper().split()
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
    if guess in choices_left and len(guess) == 1:
        for i in range(len(choices_left)):
            if choices_left[i] == guess:
                choices_left[i] = ' '
    elif len(guess) > 1:
        print("Invalid Entry, try again")
        guess = input('Pick a letter: ').upper()
        check_letter_availability(choices_left, guess)
    else:
        print(f"You've picked {guess} already, try again")
        guess = input('Pick a letter: ').upper()
        check_letter_availability(choices_left, guess)
    return guess


# check if guessed letter is right or wrong
def guess_the_letter(partial_answer, answer, guesses, letters):
    print(f'Letters available:\n{" ".join(letters)}\n')
    user_guess = input('Pick a letter: ').upper()
    user_guess = check_letter_availability(letters, user_guess)
    if user_guess in answer:
        for i in range(len(answer)):
            if user_guess == answer[i]:
                partial_answer[i] = answer[i]
        cls()
        print(f'{"Nice guess!"}\n')
        print(f'"{" ".join(partial_answer)}"\n')
        if " __ " not in partial_answer:
            cls()
            print("You guessed all the letters!!!")
            print(f'The Mystery Word was: \n{"".join(answer)}\n')
            print("YOU WON!    " * 50)
            for i in range(len(ALL_LETTERS)):
                if letters[i] == ' ':
                    letters[i] = ALL_LETTERS[i]
            try_again(letters)
        if guesses > 0:
            guess_the_letter(partial_answer, answer, guesses, letters)
    else:
        cls()
        guesses -= 1
        print(f'Sorry, {user_guess} is not in the Mystery Word. You have {guesses} guesses left!\n')
        print(f'"{" ".join(partial_answer)}"\n')
        if guesses > 0:
            guess_the_letter(partial_answer, answer, guesses, letters)
        else:
            cls()
            print(f'{"You are out of guesses"}\n')
            print(f'The Mystery Word was: \n\n{"".join(answer)}\n\n')
            print(f'{"GAME OVER"}\n')
            try_again(letters)


def try_again(letters):
    again = input('Would you like to play again? [Y/N] ').upper()
    if again != 'Y' and again != 'N':
        print("Invalid Entry")
        try_again(letters)
    else:
        if again == 'Y':
            play_game(letters)
        else:
            exit()


if __name__ == "__main__":
    play_game(initial_list_for_letters)
