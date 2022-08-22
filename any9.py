def migratoryBirds(arr):
    # Write your code here
    dict={}
    for i in arr:
        if i in dict:
            dict[i]=dict[i]+1
        else:
            dict[i]=1
    print(dict)
    count=0
    for i in dict:
        if count>0:
            if dict[i]==dict[count]:
                if i<count :
                    count=i
                    continue
                else:
                    continue
        if dict[i] > count:
            count=i
        
    
    return count


n=int(input())
1
print(migratoryBirds(arr))