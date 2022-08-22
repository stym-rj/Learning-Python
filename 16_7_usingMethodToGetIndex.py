#a Method is a function associated with specific class.

text="hello & hi"
print("1: " + str(text.index("&")))      #index() function will search for the keyword inside it in the string.
print("2: " + str(text.index("h")))
print("3: " + str(text.index("hi")))
print("4: " + str(text.index("el")))
# print("5: " + str(text.index("Hi")))     #this will give error since no letter like 'H' is present
# print("6: " + str(text.index("ho")))     #this will give error since no word of piece of word is 'ho'
print("7: " + str(text.index(" ")))