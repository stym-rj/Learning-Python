#isnumeric() methos tells us weather a string contains only numbers or not.

text1="12347235"
text2="123%32"
text3="123abc123"
print(text1.isnumeric())        #true
print(text2.isnumeric())        #false
print(text3.isnumeric())        #false