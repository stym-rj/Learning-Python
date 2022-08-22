class Animal:
    sound=""
    def __init__(self, name):
        self.name=name
    def speak(self):
        print("{sound} i m {name}! {sound}".format(name=self.name, sound=self.sound))

class Piglet(Animal):
    sound= "oink!"

piggy=Piglet("pigguu")
piggy.speak()

class Cow(Animal):
    sound="maow!"

gaay=Cow("gaaay")
gaay.speak()



goat=Animal("bakri")
goat.speak()