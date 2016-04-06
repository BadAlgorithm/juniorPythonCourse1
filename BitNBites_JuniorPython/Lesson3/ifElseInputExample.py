conditionNumber = 100
userInput = int(input("Select a number: "))
if userInput < conditionNumber:
    print("You typed in a number less than " + str(conditionNumber))
else:
    print("You typed in a number greater than " + str(conditionNumber))
print("The difference between the condition and your number is: " + str(conditionNumber - userInput))
