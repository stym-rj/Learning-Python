N=int(input())

for i in range(1,N+1):
    for k in range(1,i+1):
        print(k, end = "")
        if(k<i):
            print(",", end = "")
    print("")

for i in reversed(range(1,N+1)):
    for k in range(1,i):
        print(k, end = "")
        if(k<i-1):
            print(",", end = "")
    print("")