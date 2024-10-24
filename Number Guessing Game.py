"""
Project 2: Number Guessing Game by Hasan Mahmud
Full Stack Web Development with Python, Django & React-Batch 2
"""
import random

secret_number = random.randint(1, 100) #1. Random Number Generation:
print("Welcome to the Number Guessing Game!\nTry to guess the number between 1 and 100\n")
    
try:
    guess = int(input("Enter Your guess: ")) #2. Implement User Input Handling:
    i = 1
    while guess != secret_number: #3. Loop to continuously prompt until they correctly identify the number.
        if (1<= guess <=100):
            if guess < secret_number: #4. Conditional Logic:
                print("Too low")
            else:
                print("Too high")
                        
            print() # Print an empty line to tidy up the console for new guesses
        else:
            print("Please Enter a number from 1 to 100")
        i += 1    
        guess = int(input("Enter Your guess: "))  # Get a new guess from the user
           
    print("Congratulations! You've guessed the number in", i, "attempts.") #5. Ending the Game:
    
except ValueError:
    print("Invalid input! Please Run the game and enter a number from 1 to 100")
