var1 = "Hello"
var2 = 0
for i in range(0, 2):
    var1 += var1
for j in range(0, 256):
    var2 += 2
letter = var1[4]
newMessage = var1 + letter + var2
print(newMessage)
