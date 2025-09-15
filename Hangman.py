import random

word_list = ['data science', 'machine learning', 'python', 'code alpha']

word = random.choice(word_list)
word_length = len(word)

# Initialize guessed_word with '_' for letters and ' ' for spaces
guessed_word = ['_' if char != ' ' else ' ' for char in word]
attempts = word_length + 3
guessed_letters = []

print("Welcome to Hangman!")
print(' '.join(guessed_word))

while attempts > 0:
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try again.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print(f"Yes, '{guess}' is in the word!")
        for i in range(word_length):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print(f"No, '{guess}' is not in the word.")
        attempts -= 1

    print(' '.join(guessed_word))

    if '_' not in guessed_word:
        print("Congratulations! You've guessed the word:", word)
        break

    print(f"Attempts remaining: {attempts}")

if attempts == 0:
    print("Game over! The word was:", word)
