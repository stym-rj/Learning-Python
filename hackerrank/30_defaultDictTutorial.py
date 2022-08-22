from collections import defaultdict

t=input()
t1=t.split(" ")

n=int(t1[0])
m=int(t1[1])

listN=[]
for i in range(n):
    z=input()
    listN.append(z)

listM=[]
result=defaultdict(list)
for i in range(m):
    count=0
    z=input()
    for j in range(n):
        if z==listN[j]:
            count+=1
            result[z].append(j+1)
    if count==0:
        result[z].append(-1)

for i in result.items():
    for j in i[1]:
        print(j, end=" ")
    print()