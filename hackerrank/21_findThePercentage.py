n= int(input())

dict={}
for i in range(n):
    string=input()
    s=[]
    s=string.split(" ")
    name=s[0]
    marks=[]
    for i in range(3):
        marks.append(float(s[i+1]))
    dict[name]=marks

query=input()
for name,marks in dict.items():
    if name==query:
        sum=0
        for i in marks:
            sum+=i
        print("{:.2f}".format(sum/3))