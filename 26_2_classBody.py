class Apple:
    color=""                        #these are called as 'attributes'
    flavor=""                       ##these are called as 'attributes'

laal_seb=Apple()            #these are called objects of the class(here, object of the 'Apple' class is 'laal_seb')          #they are used similar to the functions
laal_seb.color="red"
laal_seb.flavor="sweet"             #attributes and functions of the class can be accessed using the 'dot notation' (.)

print(laal_seb.color)
print(laal_seb.flavor)
print(laal_seb.flavor.upper())


print("second object")

hra_seb=Apple()
hra_seb.color="green"
hra_seb.flavor="sour"

print(hra_seb.color)