def f(n):
    sum_of_fact=0
    for i in str(n):
        fact=1
        i=int(i)
        for j in range(1,i+1):
            fact=fact*(j)
        sum_of_fact=sum_of_fact+fact
    return sum_of_fact
    


def sfn(sum_of_fact):
    sum_of_sfn=0
    for i in str(sum_of_fact):
        i=int(i)
        sum_of_sfn=sum_of_sfn+ i
    return sum_of_sfn


def g(n):
    for i in range(1,n):
        k=f(i)
        l=sfn(k)
        f_n=f(n)
        sfn_n=sfn(f_n)
        if l==sfn_n:
            return i


def sgi(gn):
    sum_of_gn=0
    for i in str(gn):
        i=int(i)
        sum_of_gn=sum_of_gn+i
    return sum_of_gn


def final(n,m):
    last=0
    for i in range(1,n+1):
        last=last+sgi(g(i))
    return last%m


last=[]
for i in range(int(input())):
    n, m=map(int,input().split())
    last.append(final(n,m))
for i in last:
    print(i)
#factorial== f(n)
# sum_of_fact=f(n)
# print(sum_of_fact)


# s(f(n))
# sum_of_sfn=sfn(sum_of_fact)
# print(sum_of_sfn)


# g(s(f(n)))
# print(gn)


#s(g(s(f(n))))

