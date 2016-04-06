nestedList = [["hello", "hi", "g'day", "greetings"], ["goodbye", "cya", "bye"]]
for listItem in nestedList:
    print("before the inner loop")
    for word in listItem:
        print(word)
    print("after the inner loop")


