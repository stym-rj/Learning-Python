# strip() excludes spaces(whitespaces), tabs and newline character at the beginning and starting of the string.

input="    hello    "
print(input.strip()+"__")
text="  bro   brother   "
print(text.strip()+"__")

print("__"+ text.lstrip()+"__")         #excludes whitespaces only on left side of the string
print("__"+text.rstrip()+"__")          #excludes whitespaces only on right side of the string