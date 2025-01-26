
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("You have 5 chances to guess the correct number.")
print()
print()

print("Please select the difficulty level: ")
print("1. Easy (10 chances)")
print("2. Medium (5 chances)")
print("3. Hard (3 chances)")
attempts = 0
#Difficulty options
while True:
    choice = input("Enter your choice: ")
    if choice == "1":
        print()
        print()
        print("Great! You have selected the Easy difficulty level.")
        print("Let's start the game!")
        attempts = 10
        break
    elif choice == "2":
        print()
        print()
        print("Great! You have selected the Medium difficulty level.")
        print("Let's start the game!")
        attempts = 5
        break
    elif choice == "3":
        print()
        print()
        print("Great! You have selected the Hard difficulty level.")
        print("Let's start the game!")
        attempts = 3
        break

#Generates a number from 1-100
import random
number = random.randint(1,100)
#Gives a specific number of guesses depending on the difficulty you pick.
Guess = int(input("Enter your guess: "))
while attempts > 0:
    if Guess < number:
        print(f"Incorrect! The number is greater than {Guess}.")
        attempts -= 1
    elif Guess > number:
        print(f"Incorrect! The number is less than {Guess}")
        attempts -= 1
    elif Guess == number:
        print("Congratulations! You guessed the correct number")
        break

    Guess = int(input("Enter your guess: "))        

