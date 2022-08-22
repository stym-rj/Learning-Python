import datetime

now = datetime.datetime.now()       #'datetime' module has a 'datetime' class which has a 'now()' method.

print(type(now))

print(now)          #behind the scenes, the print function is calling the '__str__' method of the 'datetime' class
print(now.year)
print(now+ datetime.timedelta(days=8))