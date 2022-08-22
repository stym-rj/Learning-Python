june=30
print("june has "+ str(june)+ " days.")
july=31
print("july has "+ str(july)+ " days.")
#the above code can get too lengthy.
#to avoid our code to getting lengthy, we can make functions and reuse our code like below:-

def month_days(month, days):
    print(month + " has " + str(days)+ " days.")

month_days("june", 30)
month_days("july", 31)