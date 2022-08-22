# in for loops, the variable is automatically incremented everytime it enters the looop.

n=5
for x in range(n):      #here, FOR range() function, the default value of x will be set to 0 and the maximum value that x can reach using this loop is (n-1). #hence, this for loop will make values of x as 0,1,2,3,4. The range() is an in-built function in Python. It returns a sequence of numbers starting from zero and increment by 1 by default and stops before the given number.
    print(x)