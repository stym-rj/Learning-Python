n=int(input())
l2=[]
for i in range(n):
    string=input()
    list=[]
    list=string.split(" ")
    if list[0]=="insert":
        l2.insert(int(list[1]), int(list[2]))
    elif list[0]=="append":
        l2.append(int(list[1]))
    elif list[0]=="print":
        print(l2)
    elif list[0]=="remove":
        l2.remove(int(list[1]))
    elif list[0]=="sort":
        l2.sort()
    elif list[0]=="pop":
        l2.pop(len(l2)-1)
    elif list[0]=="reverse":
        l2.reverse()