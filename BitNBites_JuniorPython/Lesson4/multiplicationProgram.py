number1 = int(input("number 1: "))
number2 = int(input("number 2: "))
result = 0
for i in range(number2):
    result += number1
print(str(number1) + " times " + str(number2) + " equals " + str(result))