phonebook = {"thomas": "0473847624", "jim": "0472653782", "tony": "0463724190"}
userOption = input("would you like to read or add to the phonebook [r/a]?")
message = ""

SENTINEL = "-"

if userOption == "r":
    searchName = str(input("who's number would you like to search? "))
    number = phonebook[searchName.lower()]
    message = searchName + " : " + number
    print(message)
elif userOption == "a":
    print("add a new phonenumber: ")
    newName = input("Name: ")
    newNumber = input("Phone number: ")
    while newName != "-" and newNumber != "-":
        phonebook[newName.lower()] = newNumber
        print("add another phonenumber: ")
        newName = str(input("Name: "))
        newNumber = input("Phone number: ")
    print("updated phonebook:")
    for key in phonebook:
        print(key + " : " + phonebook[key])
else:
    print("invalid option")