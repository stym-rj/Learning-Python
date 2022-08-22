def convert_seconds(seconds):
    hours=seconds//3600
    minutes=(seconds-hours*3600)//60
    remaining_seconds=seconds-minutes*60- hours*3600

    return hours, minutes, remaining_seconds

result=convert_seconds(5000)
print(result)           #this is a list

hours, minutes, seconds= result             #this is called unpacking of tuples. this is done to seperate the values in a tuple.
print(hours, minutes, seconds)              #now, these values are seperated.
print(hours)


h,m,s=convert_seconds(2000)             #these will be seperated since we are giving seperate variables for each return variables of the function.
print(h,m,s)

# h1,m1=convert_seconds(3000)             #this will throw error since the function is returning 3 variables, but we are only allocating 2 variables to it.