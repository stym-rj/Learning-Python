n, m = map(int,input().split())
if n>5 and n<101 and m>15 and m<303:
    if n%2!=0:
        for i in range((n//2)):
            print((".|."*(i*2+1)).center(m, "-"))
        print("WELCOME".center(m,"-"))
        for i in reversed(range((n//2))):
            print((".|."*(i*2+1)).center(m, "-"))