# multiple=[]
# for i in range(1, 11):
#     multiple.append(i*7)
# print(multiple)

#the above code can print multiples of 7, but that is a very long way to do this.
#python gives us a feature of list comprehension through which we can do the same task in just 1 line of code.
#the below code is an example of list comprehension

multiple=[i*7 for i in range(1,11)]
print(multiple)