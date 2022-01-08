#Import Libraries
import random
import art
import os
#Weclome msg
os.system('clear')
print(art.welcome)
print("Welcome to the Number Guessing Game!!\n")

#Random number Generation
number=random.randint(1,100)
print("I am thinking if a number between 1-100.\n")

#Choice of easy of Hard to start the Game
choice=input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()
#Act on the choice
if choice=='hard':
    number_of_guess=5
else:
    number_of_guess=10

#In Loop, Allow user to make a Guess
#Check if Correct and Declare Result
while number_of_guess:
    guess=int(input("\nMake a guess : "))
    if guess == number:
        number_of_guess = 1
        print(f"\nCongratulations!! You guessed it right, it is {guess}!!\n")
        print(art.congrats)
    elif guess > number:
        print("Guess is too HIGH")
    else:
        print("Guess is too LOW")

    number_of_guess -= 1
