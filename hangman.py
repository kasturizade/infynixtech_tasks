import random

words = ["python", "computer", "programming", "developer", "internship"]

word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

print("Welcome to Hangman!")
print("Guess the hidden word one letter at a time.")
print("You have 6 incorrect guesses.\n")

while incorrect_guesses < max_guesses:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)

    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!\n")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")
        print("Incorrect guesses:", incorrect_guesses, "/", max_guesses)
        print()

else:
    print("Game Over!")
    print("The word was:", word)