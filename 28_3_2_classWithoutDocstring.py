class Piggy:
    name="Piggy"
    def speak(self):                #this is methon. a method is a function that operates on a single instance of an object.
        print("oink! oink!")
    def speak_name(self):
        print("oink! i m {}. oink!".format(self.name))

help(Piggy)