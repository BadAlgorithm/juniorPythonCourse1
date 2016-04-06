distance  = 45000
strideLength = 2.31
# initialize steps and distance travelled to 0
numberOfSteps = 0
distanceTravelled = 0
while distanceTravelled < distance:
    distanceTravelled += strideLength
    numberOfSteps += 1
print("the number of steps taken was " + str(numberOfSteps))
