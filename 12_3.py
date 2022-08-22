def get_username():
	return input()


def valid_username(username):
    if len(username)<3:
        return False
    elif len(username)>10:
        return False
    else:
        return True

username= get_username()
while not valid_username(username):
	print("Invalid username")
	username= get_username()