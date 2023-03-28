import random
import string

list_of_words = ['python', 'java', 'swift', 'javascript']

tries = 0
tmp = []
won = 0
lost = 0

random_word = random.choice(list_of_words)

print("H A N G M A N\n")

while True:
    word_to_guess = list('-' * len(random_word))

    choice = input('Type "play" to play the game, "results" '
                       'to show the scoreboard, and "exit" to quit: ')
    if not choice:
        continue

    while True:

        if choice == 'play':

            print(''.join(word_to_guess))
            guessed_letter = input('Input a letter: ')

            if len(guessed_letter) >= 2 or not guessed_letter:
                print("Please, input a single letter.")
                continue

            if guessed_letter != guessed_letter.lower() \
                    or guessed_letter not in string.ascii_letters:
                print("Please, enter a lowercase letter from the English alphabet.")
                continue

            if guessed_letter in tmp:
                print("You've already guessed this letter.")
                tries += 1

            if guessed_letter in random_word:
                for index, letter in enumerate(random_word):
                    if letter == guessed_letter:
                        word_to_guess[index] = guessed_letter
                        tmp.append(guessed_letter)
            else:
                print("That letter doesn't appear in the word.\n")
                tries += 1
                tmp.append(guessed_letter)

            guessed_word = ''.join(word_to_guess)

            if guessed_word == random_word:
                print(f"You guessed the word {random_word}!")
                print("You survived!")
                tries = 0
                won += 1
                tmp.clear()
                break
            elif tries == 8:
                print("You lost!")
                tries = 0
                lost += 1
                tmp.clear()
                break
        elif choice == 'results':
            print(f"You won: {won} times.")
            print(f"You lost: {lost} times.")
            break
        elif choice == 'exit':
            exit(1)
