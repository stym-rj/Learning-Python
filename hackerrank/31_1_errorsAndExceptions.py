t=int(input())
for i in range(t):
    n=input()
    m=n.split(" ")
    #code
    try:
        p=int(m[0])
        q=int(m[1])
        print(p//q)
    except Exception as e:
        print("Error Code:",e)