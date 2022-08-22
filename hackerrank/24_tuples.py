import hashlib

n=int(input())

m= input()
q=m.split(" ")
t=[]
for i in q:
   t.append(int(i))
t1=tuple(t)
print(hash(t1))