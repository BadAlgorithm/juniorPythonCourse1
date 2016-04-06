"""
Guessing game, the final project for Junior Python Program for bits'n'bites
1) Generate a random number between 1 and X
2) X will be obtained from use input
3) The user will keep guessing until they right answer
4) If guess is higher, say "guess lower". Vice-versa for when the guess is lower
5) Keep track of how many guesses we've had
6) Keep track of all the guesses by the user
7) At the end of the game if the number of guesses is less than 5, print "well done", if the number of guesses is
   greater than 5 or less than 10, print "Good", if its greater than 10, print "unlucky"
8) At the end of the program ask the user if they would like to play again (y, n,) if they input anything other than
   y or n, say "invalid input"
"""
import random
topBound = int(input("The number chosen will go from 1 to..."))
magicNumber = random.randint(1, topBound)
userGuess = int(input("when "))