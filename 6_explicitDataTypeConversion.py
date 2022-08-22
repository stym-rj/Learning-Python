# print("name"+7.4)       #invalid

print("name "+ str(7.4))        #here , to add a float to string, we typecasted float to make it a string. this is called explicit conversion.

students= 1000
icecream= 1500

icecream_per_head= icecream/students

# print("the total number of icecream each student can get is : " + icecream_per_head)        #invalid. since we cant add string with float.
print("the total number of icecream each student can get is : " + str(icecream_per_head))
print(str(icecream_per_head) + " the total number of icecream each student can get is : ")
# print(icecream_per_head + float("the total number of icecream each student can get is : "))   #invalid

print(type(icecream_per_head))