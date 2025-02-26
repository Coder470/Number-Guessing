import random

def Welcome_Message():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 5 chances to guess the correct number.")
    print()


def difficulty_select():
    print("Please select the difficulty level: ")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")

    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            print("\nGreat! You have selected the Easy difficulty level.")
            print("Let's start the game!")
            return 10 #Easy mode
        
        elif choice == "2":
            print()
            print("Great! You have selected the Medium difficulty level.")
            print("Let's start the game!")
            return 5 #Medium Mode
        
        elif choice == "3":
            print()
            print("Great! You have selected the Hard difficulty level.")
            print("Let's start the game!")
            return 3   #Hard Mode
    

def number_guess_generator():
    number = random.randint(1,100)
    return number

def guessing(attempts,number):
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

if __name__ == "__main__":

    #Game execution
    Welcome_Message()
    attempts = difficulty_select()
    number = number_guess_generator()
    guessing(attempts,number)
