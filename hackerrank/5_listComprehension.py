def coordinates(x,y,z,n):
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if((i+j+k)!=n):
                    print("[" + str(i)+ ", "+ str(j)+ ", "+ str(k)+ "]", end="")
                    if(i==x and j==y and k==z):
                        break
                    print(", ", end="")

a=int(input())
b=int(input())
c=int(input())
n=int(input())
print("[", end="")
coordinates(a,b,c,n)
print("]")