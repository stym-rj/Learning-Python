# from contextlib import redirect_stderr


class Apple:
    def __init__(self, color, flavour):
        self.color=color
        self.flavour=flavour
    def __str__(self):                  #this will print the below string if the statement is just "print(class_object)"
        return "This is a {} apple and it tastes {}".format(self.color, self.flavour)

laal_seb=Apple("red", "sweet")

print(laal_seb.color)
print(laal_seb)
print(laal_seb.flavour)