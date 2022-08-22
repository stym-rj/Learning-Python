def pair_sum(l):
    ans=0
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if(l[i]+l[j]>=0):
                ans=ans+1
    if ans==0:
        return 0
    else:
        return ans

l=[1,0,-1,-3,4]
print(pair_sum(l))
