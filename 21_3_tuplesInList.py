def full_emails(people):
    result=[]
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result

print(full_emails([("satyam@gmail.com", "Satyam Raj"), ("raj@yahoo.com", "Raj Raj"), ("bro@example.com", "Bro Bro")]))