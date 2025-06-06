import random
n = random.choice(range(1,1000))
guesses = 0
print("Welcome to Number Guesser! Guess the number between 1-1000 or type 'exit' or 'bye' to leave.")
while True:
    guess = input("Guess the number: ").strip().lower()
    if guess == "exit" or guess == "bye":
        print("Thanks for playing!")
        break
    elif not guess.isdigit(): print("Please enter a valid number")

    elif int(guess) == n:
        print("CONGRATS, YOU GUESSED THE NUMBER!")
        print("Number of guesses:", guesses + 1)
        guesses = 0
        n = random.choice(range(1,1000))

    elif int(guess) >= n:
        print("Too high!")
        guesses += 1
    elif int(guess) <= n:
        print("Too low!")
        guesses += 1
