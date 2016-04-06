newDictionary = {"hello": "world", "welcome": "to", "bits": "and bites"}
for key in newDictionary:
    newDictionary[key + "new"] = newDictionary[key] + " Hello New"
    print(newDictionary[key])
