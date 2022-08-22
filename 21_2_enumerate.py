animals= ["sheep","cow", "cat", "dog", "elephant", "zebra"]

for index, animal in enumerate(animals):            #enumerate returns tuples of the index of element in the list and the element at that index of that list.
    print("{} - {}".format(index+1, animal))