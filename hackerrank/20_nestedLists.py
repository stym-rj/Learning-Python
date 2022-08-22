students=[]
marks=[]
names=[]
n=int(input())
for i in range(n):
    student=[]
    for j in range(2):
        if j==0:
            name=input()
            student.append(name)
            names.append(name)
        else:
            number=float(input())
            student.append(number)
            marks.append(number)
    students.append(student)
marks.sort()
count=0
for i in marks:
    if i==marks[0]:
        count+=1
        continue
    else:
        last_second=marks[count]
        break
name_list=[]
for name, mark in students:
    if mark==last_second:
        name_list.append(name)
name_list.sort()
for i in name_list:
    print(i)