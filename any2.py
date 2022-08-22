str1=input()
upper=0
lower=0
special=0
digit=0
for i in str1:
    if i>='A' and i<='Z':
        upper+=1
    elif i>='a' and i<='z':
        lower=lower+1
    elif i>='0' and i<='9':
        digit=digit+1
    else:
        special=special +1

print("UPPER="+str(upper))
print("LOWER="+str(lower))
print("DIGIT="+str(digit))
print("SPECIAL="+str(special))