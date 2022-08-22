#printing all members of domino.
for left in range(7):
    for right in range(left, 7):
        print("[ "+ str(left)+ " | " + str(right) + " ]", end=" ")
    print()