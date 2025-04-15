import random

def hangman():
    word_list = ["cat", "hand", "shoe", "close", "mouse", "fan"]
    word = random.choice(word_list).lower()
    guessed_letters = set()
    correct_letters = set(word)
    max_attempts = 5
    attempts_left = max_attempts

    print("Welcome to Hangman!")
    print("_ " * len(word))

    while attempts_left > 0 and correct_letters != guessed_letters:
        guess = input("\nGuess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            attempts_left -= 1
            print(f"Wrong guess. You have {attempts_left} attempts left.")

        # Display current word progress
        word_progress = [letter if letter in guessed_letters else "_" for letter in word]
        print(" ".join(word_progress))

    if correct_letters == guessed_letters:
        print(f"\nCongratulations! You guessed the word '{word}'!")
    else:
        print(f"\nGame over! The word was '{word}'.")

# Run the game
hangman()
