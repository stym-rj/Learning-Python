class Piglet:
    """Represents a piglet that can say their name"""
    name="Piggy"
    def speak(self):                #this is methon. a method is a function that operates on a single instance of an object.
        """Outputs the sound of a piglet"""
        print("oink! oink!")
    def speak_name(self):
        """Outputs a sound and the name of the piglet"""
        print("oink! i m {}. oink!".format(self.name))


help(Piglet)