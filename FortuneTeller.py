
import random

'''    
    prints personal random greeting
    
    Parameters:
    name (str), name of the user
'''
def getGreeting(name):
    greetingList = ["Hello and welcome, " + name, f"Oh, hello, {name}.", f"{name}....", "Would you like to receive a fortune, " + name + "?"]
    print(random.choice(greetingList))

'''
    prints fortune based off your number
    
    Parameters:
    number (int) A random number the user picks
'''
def getFortune(number): #prints fortune
    if (1 <= number <= 28):
        print("You will have wonderful luck.")
    elif (29 <= number <= 55):
        print("You will have terrible luck.")
    elif (56 <= number == 60):
        print("You will become rich.")
    elif (61 <= number == 83):
        print("You will encounter a mountain lion! Be careful.")
    elif (84 <= number <= 100):
        print("Oh... The stars are unsure.")
    else:
        print("Please enter a valid response.")

'''
    runs the game recursively
'''
def runGame(): #runs game recursively...
    name = input("Enter your name: ")
    getGreeting(name)
    number = int(input("Choose a number between 1 and 100: "))
    getFortune(number)
    play = int(input("Enter -1 to play again! Enter any number to quit"))
    if play == -1:
        runGame() #game runs again when
    else:
        print("Thanks for playing!")


runGame()