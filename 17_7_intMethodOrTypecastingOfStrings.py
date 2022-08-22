#int() method converts a string with only numbers to an actual int datatype.

text1="3425"
text2="32ab53"
print(int(text1))
print(type(text1))
print(type(32345))
print(type("32345"))
# print(int(text2))           #this will give error since there are few non numeric characters in the text2 string.
print(int("75575"))