from itertools import permutations
n=input()
m=int(input())
listGenerated=list(permutations(n,m))
final=[]
for i in listGenerated:
    first, second=i
    temp=first+second
    final.append(temp)
final.sort()
for i in final:
    print(i)