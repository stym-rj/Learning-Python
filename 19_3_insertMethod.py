fruits=["banana", "apple" , "pineapple"]

fruits.insert(0, "kiwi")
print(fruits)

fruits.insert(3, "orange")
print(fruits)

fruits.insert(15, "peach")              #if parameter exceedes the number of element in the list then the inserted element is added at the last of the list.
print(fruits)

#usually, we add an element at the start of the list using insert(0, "element") and add an element at the end of the list using append("element")
# fruits.insert("melon")      #this is wrong since we are not specifing the place where the element need to be inserted.