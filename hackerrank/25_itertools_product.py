from itertools import product

def listmaker():
    n=input()
    m=n.split(" ")
    list1=[]
    for i in m:
        q=int(i)
        list1.append(q)
    return list1

a=listmaker()
b=listmaker()

for i in (list(product(a,b))):
    print(i, end=" ")