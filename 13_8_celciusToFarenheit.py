def to_farenheit(celcius):
    return (celcius*9/5)+32

for celcius in range(0, 101, 10):       #there are 3 parameters in range() function. the 1st and 2nd are for lower and upper limits and the 3rd one is the difference between two consecutive values in range.( that means, range will have values as : 0,10,20,30,40... and so on). In short, the variable will be incremented by the 3rd parameter which is 10 in this case.
    print(celcius, to_farenheit(celcius))