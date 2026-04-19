import random

words = ["apple", "tiger", "chair", "table", "plant"]
word = random.choice(words)

guessed_letters = []
attempts = 6

print("Welcome to Hangman!")

while attempts > 0:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if all(letter in guessed_letters for letter in word):
        print("You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("Already guessed!")
    elif guess in word:
        guessed_letters.append(guess)
        print("Correct!")
    else:
        guessed_letters.append(guess)
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

if attempts == 0:
    print("appleYou lost! The word was:", word)