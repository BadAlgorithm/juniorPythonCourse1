people = ["Billy", "Bobby", "Martha", "Kylie", "Johnny", "Casey"]
# people[0] = people[0] + " id: " + str(1)
# people[1] = people[1] + " id: " + str(2)
# people[2] = people[2] + " id: " + str(3)
# people[3] = people[3] + " id: " + str(4)
# people[4] = people[4] + " id: " + str(5)
# people[5] = people[5] + " id: " + str(6)
print(people)

# Iteration
for i in range(len(people)):
    people[i] = people[i] + " id: " + str(i)

for i in range(len(people)):
    print(people[i])

# for in loop
for person in people:
    print(person)
