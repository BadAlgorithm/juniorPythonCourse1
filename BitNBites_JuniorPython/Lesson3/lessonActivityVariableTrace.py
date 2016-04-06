a = "123445"
b = "This is another string"
c = [1, 2, 15, 16, 2]
b = b + " add me"
number1 = int(a[1])
number2 = c[3]
number3 = 1
if number2 > number1:
    number3 = number2 - number1
elif number2 < number1:
    number3 = number1 - number2
else:
    number3 = number3 * 5
print(b)
print(number1)
print(number3)
