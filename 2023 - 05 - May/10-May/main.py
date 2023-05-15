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
my_string = "".join(
    [i if i.islower() else " " + i.lower() if i in ["N", "I"] else " " + i for i in my_string]
    )[1:]
print(my_string)"""

# simple way to add list into dictionaries

"""names = ['Aish', 'Soumya', 'Ria']
prof = ['Programmer', 'Gamer', 'Designer']
my_dict = {}
#for (key, value) in zip(names, prof):
    #my_dict[key]=value
for i in range(len(names)):
    my_dict[names[i]] = prof[i]
print(my_dict)
"""

# Dictionary Comprehension

"""names = ['Aish', 'Soumya', 'Ria']
prof = ['Programmer', 'Gamer', 'Designer']
# my_dict = {key : value for (key, value) in zip(names, prof)}
my_dict = {names[i] : prof[i] for i in range(len(names))}
print(my_dict)
"""

my_dict = {
    "Spider" : 
}





