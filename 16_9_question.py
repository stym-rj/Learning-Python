from dataclasses import replace


def replace_domain(email, old_domain, new_domain):
    if "@"+old_domain in email:
        new_email=email[: email.index("@"+old_domain)]+ "@"+ new_domain
        return new_email

email="satyamraj7891@gmail.com"
old_domain="gmail.com"
new_domain="outlook.com"

print(replace_domain(email, old_domain, new_domain))