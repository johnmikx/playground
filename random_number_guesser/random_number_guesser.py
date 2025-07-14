import random

number = random.randint(1, 10)
guess = int(input("Guess a number (1-10): "))

if guess == number:
    print("Congratulations! You guessed it right.")
else:
    print("Sorry, the correct number was", number)

print("Try again with different numbers!")
print("This is a simple random number guessing game.")
print("You can improve your guessing skills with practice.")
print("Using the random module is fun.")
print("Goodbye!")