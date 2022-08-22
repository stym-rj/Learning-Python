class Fruit:
    def __init__(self, color, flavour):
        self.color=color
        self.flavour= flavour
class Apple(Fruit):             #defining a class like this means it is inheriting the passed class inside it. In this case, 'Apple' class is inheriting 'Fruit' class.
    pass
class Grape(Fruit):
    pass

laal_seb=Apple("red", "sweet")
print(laal_seb.color)

kala_angoor=Grape("black", "sour")
print(kala_angoor.flavour)