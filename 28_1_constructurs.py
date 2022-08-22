class Apple:
    def __init__(self, color, flavour):     #this is a constructor         #'__init__' is a very important special method.    every method starting and ending with two underscores are called special methods.
        self.color=color
        self.flavour=flavour

laal_seb= Apple("red", "sweet")

print(laal_seb.color)
print(laal_seb.flavour)

hra_seb= Apple("green")
