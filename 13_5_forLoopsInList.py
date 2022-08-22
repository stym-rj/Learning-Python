#to find some of few numbers.

values= [3,4,5,2,5,2,3,6]
sum=0
for x in values:
    sum+=x
print("the sum of all the values is : "+ str(sum))
print("the average of all the values is : "+ str(sum/len(values)))
print("sum= "+str(sum) + "\n" + "average= " + str(sum/len(values)))