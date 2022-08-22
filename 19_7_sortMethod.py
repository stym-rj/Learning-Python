#the sort() function returns the elements of the list in ascending form

num=[1,2,6,3,5,2,6,]
print(num)
num.sort()          #if no parameters are passed in sort() function, then by default it makes the list in ascending order
print(num)

animals=["sheep", "cow", "elephant", "bear"]
animals.sort()          #for a list of strings, by default it sorts the elements on the basis of first letter of the string.
print(animals)

def length(s):
    return len(s)
cars=["swift", "ambassador", "BMW"]
cars.sort(key=length)           #to sort a list on basis of something. Like for example, here we have sorted the list on the basis of length of the elements by using a function.
print(cars)