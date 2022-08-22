import calendar

n=input().split(" ")
month=int(n[0])
day=int(n[1])
year=int(n[2])

p=calendar.weekday(year, month, day)

# print(p)

if p==0:
    print("MONDAY")
elif p==1:
    print("TUESDAY")
elif p==2:
    print("WEDNESDAY")
elif p==3:
    print("THURSDAY")
elif p==4:
    print("FRIDAY")
elif p==5:
    print("SATURDAY")
elif p==6:
    print("SUNDAY")