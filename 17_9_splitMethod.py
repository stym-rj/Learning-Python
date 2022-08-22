#split() Method returns a list of strings that is automatically seperated where ever there is a whitespace(which is default and can be changed)

text1=" this is a laptop my friend"
print(text1.split())
print(text1.split(" "))
print(text1)

text2="hel-lo my fr-iend, -ho-w are yo-u?"
text3=text2.split("-")
print(text3)
print(text3[0])
print(len(text3))