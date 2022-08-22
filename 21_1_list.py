animals=["dog", "cat", "elephant", "cow", "sheep"]

count=0
for animal in animals:
    count+=len(animal)

print("total number of chracters : {}       average : {}".format(count, count/len(animals)))