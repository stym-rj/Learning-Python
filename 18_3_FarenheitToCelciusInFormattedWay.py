def to_celcius(farenheit):
    return (farenheit-32)*(5/9)


#this is the bad/dirty way:
print()
print("bad way".center(40, "-"))
print()
for farenheit in range(0, 101, 10):
    print(farenheit, to_celcius(farenheit))



#below is the good way:
print()
print("good way".center(40, "-"))
print("{:^40}".format("good way"))
print()
for farenheit in range(0, 101, 10):       #there are 3 parameters in range() function. the 1st and 2nd are for lower and upper limits and the 3rd one is the difference between two consecutive values in range.( that means, range will have values as : 0,10,20,30,40... and so on). In short, the variable will be incremented by the 3rd parameter which is 10 in this case.
    print("{:>6} F | {:>6.2f} C".format(farenheit, to_celcius(farenheit)))