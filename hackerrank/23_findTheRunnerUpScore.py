b=int(input())
n=input()
m=n.split(" ")
q=[]
for i in m:
    q.append(int(i))

q.sort()

for i in range(b):
    if q[b-i-1]==q[b-i-2]:
        continue
    else:
        print(q[b-i-2])
        break