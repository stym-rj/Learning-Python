s=["my", "name", "is", "satyam"]
print(type(s))
print(s)
print(len(s))

print("is" in s)
print("raj" in s)
print("" in s)
print(s[3])
# print(s[5])         #will give error

i=len(s)
print(s[1:i-1])
print(s[1:])
print(s[:i])