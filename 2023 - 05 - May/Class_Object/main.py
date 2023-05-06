"""class Fruit :
    def __init__(self) :
        self.name = "Apple"
        self.color = "Red"

fruit = Fruit()

fruit.color = "green"
print(fruit.color)
"""

# passing parameter & attributes
"""class Fruit:
        def __init__(self, name, clr):
            self.name = name
            self.colour = clr

apple = Fruit("apple", "red")
banana = Fruit("Banana", "Yellow")

print(banana.colour)"""

# methods

"""class Fruit :
    def __init__(self, name, clr) :
        self.name = name
        self.colour = clr
        self.exp_date = "12-May"

    def details(self) :
        print("My " + self.name + " is " + self.colour + ". It will expire on " + self.exp_date)


apple = Fruit("apple", "red")
banana = Fruit("Banana", "Yellow")

apple.details()
banana.details()"""

# __init__ method

"""class my_class:
    def __init__(self): # __init__ initialize attributes here bcz it auto execute with every new object , self - detect the current object
        self.attr = []

"""

"""class guiter :
    def __init__(self) :
        self.n_string = 6  # attribute
        self.play()
    def play(self) :  # self parameter inside the new function makes it a method
        print("aihjsdghuid daiuwhiuaed weuaihuw")
my_Guiter = guiter()"""


#inheritance

#parent class
class Guiter :
    def __init__(self, n_string) :
        self.n_string = n_string  # attribute
        self.play()
        self.__cost = 50
    def play(self) :  # self parameter inside the new function makes it a method
        print("Pa para parappa pappa pa pa pa ")

def BassGuiter (Guiter) :


#child class
class ElectricGuiter(Guiter): #inheriting everything from Guiter class
    def __init__(self): # changing something from parent class
        super().__init__() #allowing the subclass to override methods or attributes of parent class and provide its own implementation.
        self.n_string = 8
        self.color = ("#000000", "#FFFFFF") #adding new attribute

    def __secret(self):
        print("This Guiter actually cost me $", self._Guiter__cost, "Only!")

    def playlowder(self): # adding something to it
        print("Pa para parappa pappa pa pa pa".upper())



child_class = ElectricGuiter()

print("child class : ", child_class.n_string)
print("Parent Class : ", Guiter().n_string)

child_class._ElectricGuiter__secret()


"""class Animal :
    def __init__(self, name) :
        self.name = name

    def speak(self) :
        print(f"{self.name} says hello")

class Dog(Animal) :
    def __init__(self, name, breed) :
        super().__init__(name)
        self.breed = breed

    def speak(self) :
        super().speak()
        print("Woof")


my_dog = Dog("Fido", "Labrador")
my_dog.speak()
"""

