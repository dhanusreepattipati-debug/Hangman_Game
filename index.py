import random

# Step 1: Create word list
words = ["python", "apple", "tiger", "chair", "robot"]

# Step 2: Select random word
secret_word = random.choice(words)

# Step 3: Create display with underscores
display = ["_"] * len(secret_word)

# Step 4: Variables
wrong_guesses = 0
max_wrong_guesses = 6
guessed_letters = []

print("=== Welcome to Hangman Game ===")

# Step 5: Game loop
while wrong_guesses < max_wrong_guesses and "_" in display:

    # Show current word
    print("\nWord:", " ".join(display))

    # Take input
    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet.")
        continue

    # Check repeated guess
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Store guessed letter
    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in secret_word:
        print("Correct guess!")

        # Reveal letters
        for index in range(len(secret_word)):
            if secret_word[index] == guess:
                display[index] = guess

    else:
        wrong_guesses += 1
        print("Wrong guess!")
        print("Remaining attempts:", max_wrong_guesses - wrong_guesses)

# Step 6: Final result
if "_" not in display:
    print("\nCongratulations! You guessed the word:", secret_word)
else:
    print("\nGame Over!")
    print("The word was:", secret_word)