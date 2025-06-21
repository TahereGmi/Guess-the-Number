import random

print("🎮 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100...")

# Generate Secret Random number
secret_number = random.randint(1, 100)

# Tries counter
attempts = 0

while True:
    guess_input = input("Enter your guess: ")

    # Check input validation
    # isdigit() checks if the string just contain (0-9)
    if not guess_input.isdigit():
        print("❗ Please enter a valid number.")
        # Continue to the rest of code
        continue

    # Convert input string to int number
    guess = int(guess_input)
    # Add one other try
    attempts += 1

    # Check user guess
    if guess < secret_number:
        print("📉 Too low!")
    elif guess > secret_number:
        print("📈 Too high!")
    else:
        print(f"🎉 Correct! You guessed the number in {attempts} tries!")
        break
