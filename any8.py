import random
from unicodedata import decimal

n=int(input())
binary=""
for i in range(n):
    temp=random.randint(0,1)
    binary=binary+ str(temp)
print(binary)
decimal=int(binary, 2)
print(decimal)
