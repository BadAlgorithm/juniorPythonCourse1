import random



def guessingGame():
    numGuesses = 0
    listOfGuesses = []

    upperBound = int(input("The numbers will go from 1 to... "))
    magicNumber = random.randint(1, upperBound)
    print(magicNumber)
    userGuess = int(input("Pick your first guess: "))
    numGuesses += 1
    listOfGuesses.append(userGuess)
    while userGuess != magicNumber:
        if userGuess < magicNumber:
            print("Guess Higher...")
        elif userGuess > magicNumber:
            print("Guess Lower...")
        userGuess = int(input("Pick another: "))
        numGuesses += 1
        listOfGuesses.append(userGuess)
    print("It took you " + str(numGuesses) + " guesses to get the the right answer")
    print("Your guesses: ")
    for guess in listOfGuesses:
        print(guess)
    if numGuesses < 5:
        print("well done!!!")
    elif numGuesses >= 5 and numGuesses <= 10:
        print("Good...")
    else:
        print("Better luck next time!!!")

def main():
    isPlaying = True
    while isPlaying:
        guessingGame()
        userChoice = input("Would you like to play again? [yes/no]")
        if userChoice == "yes":
            guessingGame()
        elif userChoice == "no":
            isPlaying = False
        else:
            print("invalid input")
    print("Thanks for playing the Guessing Game")

main()