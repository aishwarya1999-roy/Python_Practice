# __name--
"""import pandas as pd

df= pd.DataFrame([1, 3])
print("This is module")
print(__name__)"""

# __name__ == "__main__"

"""def callme() :
    print("Helloo!!")
if __name__ == "__main__" :  # if we add this , then the callme() function will only execute when this module is a top
    # level module, even if this program/module imported into some other program, then also the callme() module will 
    # not work. Top Level Module - The module (Any function, class) present in the current program, not imported from
    # some others program 
    callme()
"""

# modifying list using List Comprehension

"""fruits = ["apple", "grapes", "mango"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)"""

"""bits = [False, True, False, False, True, False, False, True]
bits = [1 if b == True else 0 for b in bits]
print(bits)"""

# String Manipulation

"""my_string = "HelloMyNameIsAish"
my_string = "".join([i if i.islower() else " " + i for i in my_string])
print(my_string)"""

my_string = "HelloMyNameIsAish"
print(my_string.type)

