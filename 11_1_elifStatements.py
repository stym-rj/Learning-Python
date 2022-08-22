def valid_username(username):
    if len(username)<3:
        print("Invalid username. Username must be more than 2 characters.")
    elif len(username)>10:
        print("Invalid username. Username must be less than 11 characters.")
    else:
        print("Valid username.")

username= input()
valid_username(username)