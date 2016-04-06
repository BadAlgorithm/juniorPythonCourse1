SENTINEL = "STOP"
userInput = input("What would you like to print? ")
while userInput != SENTINEL:
    print(userInput)
    userInput = input("What would you like to print? ")
print("Program ending")
