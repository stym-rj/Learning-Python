s=input()


if len(s)>0 and len(s)<1000:
    count=0
    for i in s:
        if s.isalnum():
            print(i.isalnum())
            count=1
            break
    if count==0:
        print(i.isalnum())
    count=0
    for i in s:
        if i.isalpha():
            print(i.isalpha())
            count=1
            break
    if count==0:
        print(i.isalpha())
    count=0
    for i in s:
        if i.isdigit():
            print(i.isdigit())
            count=1
            break
    if count==0:
        print(i.isdigit())
    count=0
    for i in s:
        if i.islower():
            print(i.islower())
            count=1
            break
    if count==0:
        print(i.islower())
    count=0
    for i in s:
        if i.isupper():
            print(i.isupper())
            count=1
            break
    if count==0:
        print(i.isupper())