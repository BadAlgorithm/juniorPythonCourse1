"""
Guessing game, the final project for Junior Python Program for Bits'n'Bites
1) Generate a random number between 1 and X
2) X will be obtained from user input
3) The user will keep guessing until they right answer
4) If guess is higher, say "guess lower". Vice-versa for when the guess is lower
5) Keep track of how many guesses we've had
6) Keep track of all the guesses by the user
7) At the end of the game if the number of guesses is less than 5, print "well done", if
   the number of guesses is greater than 5 or less than 10, print "Good", if its greater
   than 10, print "unlucky".
8) At the end of the program ask the user if they would like to play again (y, n,) if they
   input anything other than y or n, say "invalid input"
"""
import random

def mainGame():
    numberOfGuesses = 0
    listOfGuesses = []
    topBound = int(input("The number chosen will go from 1 to..."))
    magicNumber = random.randint(1, topBound)
    print(magicNumber)
    userGuess = int(input("What is your first guess? "))
    listOfGuesses.append(userGuess)
    numberOfGuesses += 1
    while userGuess != magicNumber:
        if userGuess > magicNumber:
            print("guess lower")
        elif userGuess < magicNumber:
            print("guess higher")
        userGuess = int(input("Pick again: "))
        listOfGuesses.append(userGuess)
        numberOfGuesses += 1
    if numberOfGuesses < 5:
        print("Well done!!!")
    elif numberOfGuesses >=5 and numberOfGuesses <= 10:
        print("Good")
    else:
        print("Better luck next time")
    print("It took you " + str(numberOfGuesses) + " guesses to get the right answer")
    print("Your guesses: ")
    for guess in listOfGuesses:
        print(guess)

def main():
    isPlaying = True
    isInputValid = False
    while isPlaying:
        mainGame()
        userChoice = input("Would you like to play again? [y,n]")
        if userChoice == "n":
            isPlaying = False
            isInputValid = True
            print("Thanks for playing the Guessing Game")
        elif userChoice == "y":
            isInputValid = True
        while not isInputValid:
            print("Invalid Input")
            userChoice = input("Would you like to play again? [y,n]")
            if userChoice == "n":
                isPlaying = False
                isInputValid = True
                print("Thanks for playing the Guessing Game")
            elif userChoice == "y":
                isInputValid = True

main()