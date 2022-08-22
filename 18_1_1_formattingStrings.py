name="satyam"
number= len(name)*3
print("hello guys i m {} . number= {}".format(name, number))        #this is similar to printing variables in c using 'printf' function.
print("hello guys i m {number} . number= {name}".format(name=name, number=len(name)*3))     #{name}, {number} is called place holders. if the variables gets messed up, we can do this. and assigning values to the variables inside format() function is neccessary.