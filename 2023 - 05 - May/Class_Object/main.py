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


# inheritance

#parent class
"""class Guitar:
    def __init__(self, n_string=6):
        self.n_string = n_string
        self.__cost = 50
    def play(self): # self parameter inside the new function makes it a "Method"
        print("I'm in parent class")

#child class
class bassGuiter(Guitar):
    pass # adding pass to copy & paste exact same from Guitar parent class

#child class
class ElectricGuitar(Guitar): # inheriting everything from Guitar class
    def __init__(self):
        super().__init__(n_string = 10) # supar() -> allowing the subclass to override methods or attributes of parent class and provide its own implementation.
        self.color = ("#FFFFFF", "#000000") # adding new attribute in child class
        #self.__cost = 50 # __cost -> __ is used to make it private

    def play_louder(self):
        print("I'm in Child class")

    def __secret(self): # private method
        print("This is Private Guitar, this cost me around $", self._Guitar__cost, "Only!")

my_guitar = ElectricGuitar()
#print("Guitar's secreat price : ", my_guitar._Guitar__cost) # _ElectricGuitar__cost or _Guitar__cost ->  <_classname> is used print private object
my_guitar._ElectricGuitar__secret()
print("In base guitar : ", bassGuiter(4).n_string)
print("In Electric guitar : ",my_guitar.n_string)"""