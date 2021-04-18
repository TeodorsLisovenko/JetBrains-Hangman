# Write your code here
import random

print("H A N G M A N")

words = ['python', 'java', 'kotlin', 'javascript']


def hangman():
    random_word = random.choice(words)

    word_to_guess = list("-" * (len(random_word)))

    guessed_letters = ""

    counter = 0

    print()

    while counter != 8:

        print("".join(word_to_guess))

        if "-" not in word_to_guess:
            break

        letter = input("Input a letter: ")
        char_counter = -1

        if not len(letter) == 1:
            print("You should input a single letter")
            print()
            continue
        elif letter.isupper():
            print("Please enter a lowercase English letter")
            print()
            continue
        elif not letter.isalpha():
            print("Please enter a lowercase English letter")
            print()
            continue

        if letter in guessed_letters:
            print("You've already guessed this letter")
            if counter != 8:
                print()
        elif letter in random_word:
            print()
            guessed_letters += letter
            for char in random_word:
                char_counter += 1
                if char == letter:
                    word_to_guess[char_counter] = letter
        else:
            counter += 1
            print("That letter doesn't appear in the word")
            guessed_letters += letter
            if counter != 8:
                print()

    if "-" not in word_to_guess:
        print(f"You guessed the word {''.join(word_to_guess)}!")
        print("You survived!")
        print()
    else:
        print("You lost!")
        print()


game_is_on = True

while game_is_on:

    play_or_exit = input('Type "play" to play the game, "exit" to quit:')

    if play_or_exit == "play":
        hangman()
    elif play_or_exit == "exit":
        game_is_on = False
