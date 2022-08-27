# packages

"""from fname import manage
manage.add(10)
"""
'''import fname.manage
fname.manage.add(10)'''

'''import random
x, y = 10, 50
print(random.randrange(x, y))'''  # random module help to find random numbers from x to y-1 using randrange

'''import math

x, y = 16, 5'''
'''
num1 = 234.01
num2 = 6
num3 = -27.01
print("The smallest integer greater than or equal to num1,", num1, ":", math.ceil(num1))
print("The largest integer smaller than or equal to num1,", num1, ":", math.floor(num1))
print("The factorial of num2,", num2, ":", math.factorial(num2))
print("The absolute value of num3", num3, ":", math.fabs(num3))

add = 3 * math.pi
print(add)
print(math.gcd(10,4))'''

# print(math.fmod(x,y))
'''
a = math.log2(10)
print(a)'''

"""import re
if re.search(r"Air", "Airline") is not None:
    s = re.sub(r'Air', r'Aish', "Airline")
    print(s)
else:
    print("Pattern not found")"""

"""song="JINGLE Bells jingle Bells Jingle All The Way"
d = song.upper()
song_words=song.split()
count=0
for word in song_words:
    if(word.startswith("jingle")):
        count=count+1
print(count)"""


# import re
"""import re
word="New Airlines4"
if re.search(r"^N", word) and re.search(r"e$", word):
    print(re.sub(r"New",r"Old",word))
else:
    print(re.sub(r"s(\d{1})",r"S\1",word))"""


"""import re
if(re.search(r"A\d?i","A33irline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")"""


# random package
"""import random
x, y = 1, 6
print(random.randrange(x, y))"""