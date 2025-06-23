import random

max_attempts = 7

print("🎮 Welcome to the Number Guessing Game!")
while True:
    mode = input("Who should guess? Type 'you' to guess or 'computer' for me to guess: ").lower()
    if mode in ["you", "computer"]:
        break
    else:
        print("❗ Invalid input. Please type 'you' or 'computer'.")

if mode == "you":

    print("I'm thinking of a number between 1 and 100...")
    print(f"You have {max_attempts} attempts. Good luck!")

    # Generate Secret Random number
    secret_number = random.randint(1, 100)

    # Tries counter
    attempts = 0

    while attempts < max_attempts:
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
    else:
        # Game over
        print(f"❌ You ran out of attempts! The correct number was {secret_number}.")

if mode == 'computer':
    print("🧠 Okay! I will guess your number.")
    # Taking bound from user
    while True:
        low_input = input("Enter the lower bound of your number: ")
        high_input = input("Enter the upper bound of your number: ")

        if low_input.isdigit() and high_input.isdigit():
            low = int(low_input)
            high = int(high_input)
            if low < high:
                break
            else:
                print("⚠️ Lower bound must be less than upper bound.")
        else:
            print("❗ Please enter valid numbers.")
    attempts = 0

    while low <= high:
        guess = (low + high) // 2
        attempts += 1
        print(f"My guess is: {guess}")

        feedback = input("Is it too high (h), too low (l), or correct (c)? ").lower()

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        elif feedback == "c":
            print(f"🎉 Yay! I guessed your number in {attempts} tries!")
            break
        else:
            print("❗ Please type 'h' for high, 'l' for low, or 'c' for correct.")
else:
    print("❌ Invalid choice. Please restart and choose either 'you' or 'computer'.")
