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

# using list/ tuple
"""names = ['Aish', 'Soumya', 'Ria']
prof = ['Programmer', 'Gamer', 'Designer']
# my_dict = {key : value for (key, value) in zip(names, prof)}
my_dict = {names[i] : prof[i] for i in range(len(names))}
print(my_dict)
"""
# using dictionaries - if we know the data of the dictionaries
"""my_dict = {
    "Spider": "photographer",
    "Bat": "philanthropist",
    "Wonder Wo": "nurse"
}
my_dict = {(key + "man" if key!= "Spider" else "Superman") : (val if val!= 'photographer' else "Journalist")for (key, val) in my_dict.items()}
print(my_dict)
"""

# if we don't know the data of the dict.
# dictionaries of lists

"""import random
bases = ["A", "T", "C", "G"]
stand1 = random.choices(bases, k = 10)
print(stand1)

dna = {key : [val, ("T" if val == "A" else "A" if val == "T" else "C" if val == "G" else "G")] for (key, val) in
       enumerate(stand1)}
print(dna)"""


# list of dictionaries
"""import random
import string
keys = ["id", "username", "password"]
users = ["Queen", "Blacy", "Lady", "Vampire"]

data = [{key: {i if key == "id" else users[i] if key == "username" else ''.join(random.choices(string.printable, k = 8))} for key in keys} for i in range(len(users))]
print(data)
"""



