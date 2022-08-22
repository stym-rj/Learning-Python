from collections import Counter
x=int(input())
list1=input()
list2=list1.split(" ")

list3=[]
for i in list2:
    m=int(i)
    list3.append(m)

tupOfShoeSize=Counter(list3).items()

dictOfShoeSize={}

for i in tupOfShoeSize:
    size, noOfShoes=i
    dictOfShoeSize[size]=noOfShoes

moneyEarned=0

orders=int(input())

for i in range(orders):
    list4=[]
    tempString=input()
    list5=tempString.split(" ")
    for j in list5:
        m=int(j)
        list4.append(m)
    
    if list4[0] in dictOfShoeSize:
        if dictOfShoeSize[list4[0]]>0:
            moneyEarned=moneyEarned+ list4[1]
            temp=dictOfShoeSize[list4[0]]
            dictOfShoeSize[list4[0]]=temp-1

print(moneyEarned)