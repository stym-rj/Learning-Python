class Piglet:
    name="Piggy"
    def speak(self):                #this is methon. a method is a function that operates on a single instance of an object.
        print("oink! oink!")
    def speak_name(self):
        print("oink! i m {}. oink!".format(self.name))

pig1=Piglet()
pig1.name="piggu"
pig1.speak()
pig1.speak_name()

pig2= Piglet()
pig2.name="Sugarwa"
pig2.speak()
pig2.speak_name()

pig3=Piglet()
pig3.speak()
pig3.speak_name()