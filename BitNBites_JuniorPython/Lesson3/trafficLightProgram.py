# %%%----------------Standard task------------------%%%
lightColour = input("Light colour: ")
if lightColour == "green":
    print("go!")
elif lightColour == "orange":
    print("slow down")
elif lightColour == "red":
    print("stop")
else:
    print("Invalid colour (must be; red, orange or green)")

# %%%----------------Extension task------------------%%%

# Logical operators
userColour = input("Light colour: ")
lightColour = userColour.upper()
if lightColour == "GREEN" or lightColour == "G":
    print("go!")
elif lightColour == "ORANGE" or lightColour == "O":
    distance = input("Are you near or far away from the lights? ")
    distanceUpper = distance.upper()
    if distanceUpper == "NEAR" or distanceUpper == "N":
        print("Keep going")
    elif distanceUpper == "FAR" or distanceUpper == "F":
        print("Prepare to stop")
else:
    print("Stop...")

# String indexing
userColour = input("Light colour: ")
lightColour = userColour.upper()
if lightColour[0] == "G":
    print("go!")
elif lightColour[0] == "O":
    distance = input("Are you near or far away from the lights? ")
    distanceUpper = distance.upper()
    if distanceUpper[0] == "N":
        print("Keep going")
    elif distanceUpper[0] == "F":
        print("Prepare to stop")
else:
    print("Stop...")
