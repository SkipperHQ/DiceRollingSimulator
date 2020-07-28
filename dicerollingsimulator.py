### AUTHOR: SkipperHQ
### DATE STARTED: 28/07/2020
### PROJECT NAME: Dice Rolling Simulator
### PROJECT DESCRIPTION: A simple dice rolling simulator with functionality to select and roll up to four dice at once, providing not only the result but the sum of the four dice at the same time.

###### Preparatory Settings ######

import random
import os
import sys

dice_one = False
dice_two = False
dice_three = False
dice_four = False

##### End of Preparatory Settings ######

# Start of Main Menu.
def main():
    print("Welcome to Anthony's Dice Rolling Simulator\nPlease navigate using the numbers to the left of their respective options.\n1. Select Dice to Roll\n2. Quit Application\n")
    userInput = input("> ")
    if userInput == "1" or userInput.title() == "Dice":
        
        # Code below allows user to select number of dice they'd like to use.
        print("How many dice would you like? Please type a number from 1 to 4.\nCurrently, only 1 to 4 dice are supported.\n")
        diceInput = input("> ")
        if diceInput ==  "1" or diceInput == "2" or diceInput == "3" or diceInput == "4":
            dice(diceInput)
        
        else:
            print("Error, please use 1-4 to choose the amount of dice you'd like. Returning to main menu.")
            main()
            
    elif userInput == "2" or userInput.title() == "Exit" or userInput.title() == "Quit":
        sys.exit()
        

# Start of dice rolling function.
def dice(diceInput):
    if diceInput == "1":
        dice_one = random.randint(1,6)
        print("The dice rolled", dice_one, "\nClick Enter to Continue...")
        input("> ")
        main()
    elif diceInput == "2":
        dice_one = random.randint(1,6)
        dice_two = random.randint(1,6)
        print("Your first dice rolled a", dice_one)
        print("Your second dice rolled a", dice_two)
        print("The sum of your two dice rolls are:", dice_one + dice_two, "\nClick Enter to Continue...")
        input("> ")
        main()
    elif diceInput == "3":
        dice_one = random.randint(1,6)
        dice_two = random.randint(1,6)
        dice_three = random.randint(1,6)
        print("Your first dice rolled a", dice_one)
        print("Your second dice rolled a", dice_two)
        print("Your third dice rolled a", dice_three)
        print("The sum of your three dice rolls are:", dice_one + dice_two + dice_three, "\nClick Enter to Continue...")
        input("> ")
        main()

    elif diceInput == "4":
        dice_one = random.randint(1,6)
        dice_two = random.randint(1,6)
        dice_three = random.randint(1,6)
        dice_four = random.randint(1,6)
        print("Your first dice rolled a", dice_one)
        print("Your second dice rolled a", dice_two)
        print("Your third dice rolled a", dice_three)
        print("Your fourth dice rolled a", dice_four)
        print("The sum of your four dice rolls are:", dice_one + dice_two + dice_three + dice_four, "\nClick Enter to Continue...")
        input("> ")
        main()

    else:
        print("Error, see dice()")
        main()
        
main()
