from itertools import permutations
n=input()
m=n.split(" ")
listGenerated=list(permutations(m[0],int(m[1])))
list1=[]
for i in listGenerated:
    list2=[]
    for items in i:
        list2.append(items)
    list1.append(list2)
list1.sort()
for j in list1:
    for k in j:
        print(k,end="")
    print("")