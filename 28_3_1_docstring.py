def to_km(meters):
    return meters/1000

def to_seconds(hours, minutes, seconds):
    """This will return the ammount of seconds in given hours, minutes and seconds."""              #The text quoted in triple quotes is called 'docstring'. docstring is defined inside triple quotes.
    return hours*60+ minutes* 60 + seconds

help(to_km)

print("--------------------------------------------------------------------")

help(to_seconds)





#docstring is usually written to give extra information about the function when it is used with the help function.