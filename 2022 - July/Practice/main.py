# conditional

"""score = input("Enter Score: ")
s = float(score)
if(s>=1.0):
    print("Score is out of range!")
elif (s >= 0.9):
    print("A")
elif (s >= 0.8):
    print("B")
elif (s >= 0.7):
    print("C")
elif (s >= 0.6):
    print("D")
elif (s < 0.6):
    print("F")"""

# function

'''def thing():
    print('Hello')
    print('Fun')

thing()
print('zip')
thing()
'''

# Arguments pass

"""big=max('Hello world')
print(big)
tiny=min('helloworld')
print(tiny)

print(float(99)/100)"""

'''x = 5
print("Hello")

def print_lyric():
    print("Maahi veh")

print('yo')
print_lyric()
x=x+2
print(x)'''

# passing parameters

"""def greet(lang):
    if lang == 'es':
        print("Hola")
    elif lang == 'fr':
        print("Bonjour")
greet('fr')"""

# return statement

"""def greet():
    return "Hello"
print(greet(), "Aish")
print(greet(), "Soumya")"""

# return statement with passing parameters

"""def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'
print(greet('fr'), 'Aish')
print(greet('en'), 'Soumya')"""

# multi parameters passing

"""def addto(a, b, c):
    add = a + b + c
    return add

print(addto(3, 5, 6))"""

"""def funv(x):
    print(x)
funv(10)
funv(20)"""

"""def sd():
    print("Hello")
    return
    print("World")

sd()"""

# while loop

"""n = 5
while n > 0:
    print(n)
    n = n - 1
print("Blast")
print(n)"""

# break

"""while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')
"""

# continue

"""while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')"""

# for loop - in

"""x= [1,2,4,6,8,9,5,7]
for i in x:
    print(i)
print("Blastoff!!")"""

# just a test

"""def check_value(message,num):
    msg=message[:num]
    print (msg)
    return len(msg)

result=check_value('Infosys',4)
print("Result:", result)"""

# largest number in a list

"""largest = 0
print("Before : ", largest)
list1 = [9, 41, 12, 3, 74, 15]
for thing in list1:
    if thing > largest:
        largest = thing
    print(largest, thing)
print("After : ", largest)"""

# smallest number in a list

"""smallest = None
print("Before : ", smallest)

list1 = [9, 41, 12, 3, 74, 15]

for thing in list1:
    if smallest is None:
        smallest = thing
    elif thing < smallest:
        smallest = thing
    print(smallest, thing)
print("After : ", smallest)"""

"""a = 0
b = 0

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        n = float(num)
    except:
        print("Invalid input")
        continue
    a=a+1
    b=b+n

print(b,a)"""

"""fruit = 'Banana'
letter = fruit[5]
print(letter)

print(len(fruit))

ind = fruit.index('na')
print(ind)"""

"""
i = 0
while i < len(fruit):
    j = fruit[i]
    print(j)
    i = i + 1

print("\n 2nd Method \n ============ \n ")

for k in fruit:
    print(k)
"""

# count number of a character present in a word

"""word = "hello, i am aishwarya Roy, currently i am working in infosys as an operation executive"
count = 0
for letter in word:
    if letter == "n":
        count = count + 1
print(count)
"""

# slicing

"""s = "Hello Python"
print(s[5:])"""

# String concatenation

'''a= 'hello'
b = a + ' ' + 'There'
print(b)'''

##################################
'''fu = 'Banana'
if 'z' in fu:
    print("True")
else:
    print("False")'''

"""fu = 'Banana'
try:
    fu[2] = "D"
except:
    if 'a' in fu:
        print("True")
    else:
        print("False")"""

###################################

"""word = 'python'
if word == "banana":
    print("All right!")
if word < 'banana':
    print('this word '+ word + ' comes before banana')
elif word > 'banana':
    print('your word ' + word + ' comes after banana')
else:
    print('All right bananas')"""

###########################

# g = "Hello world"

# upper lower

"""za = g.lower()
xa = g.upper()
print(za)
print(g)
print(xa)"""

# capitalize
# print(g.capitalize())

# find
'''po=g.find('w')
pos = g.find('o',po)
print(pos)
'''
# replace

'''repl = g.replace('Hello', 'Bye')
print(repl)'''

# strip
#  print(g.rstrip())

# startswith

'''if not g.startswith('h'):
    print("False")
'''
# endswith
"""if g.endswith('ld'):
    print("True")

if not g.endswith('Ld'):
    print("False")"""

# data = "ahdkdk jajkewih@gmail khwiiekwf 6290972895"

# parsing and extracting
"""fo=data.find('f')
print(fo)
phone= data[fo+2: ]
print(phone)
"""
# count
# print(data.count('a'))

# digit or not
'''f = '1rrtt234'
print(f.isdigit())'''

# split
"""
p = "aishwarya roy"
sp = p.split('a')
print(sp)"""

# Files

'''fh = open('ai.txt')
count = 0
for i in fh:
    count = count + 1
print(count)

le = fh.read()
print(len(le))
    for i in fh:
    i = i.rstrip()
    if i.startswith('re'):
        print(i)'''

# list

fr = ['Aish', 'soumya', 'anirban']
'''for i in fr:
    print("Hi", i)'''

"""print(fr[1])

fr[2]='ehidj'

print(fr)
print(len(fr[2]))"""

# print(fr[1][1])

'''print(range(len(fr)))

print(range(4))'''
"""for i in fr:
    print(i)
"""
"""for i in range(len(fr)):
    fri=fr[i]
    print(fri)"""

# concat list

"""a = [1, 6, 7, 8, 9]
b = [8, 5, 6, 8]
c = a + b
print(c)"""

# list slice
'''a = [3, 4, 6, 7, 8, 9]
print(a[:])'''

'''x=list()
print(type(x))
print(dir(x))'''

# building list

"""a = list()
a.append(2)
print(a)
a.append(20)
print(a)"""

# sort list
"""a=[1,3,5,8,0]
print(a)
a.sort()
print(a)"""

# list build in functions
"""a=[1,3,5,8,0]
print(len(a))
print(max(a))
print(min(a))
print(sum(a))
print(sum(a)/len(a))"""

"""a = [1, 2, [3, 5], 7, 8, 90]

print(a[2].index(5))"""

# average

"""total=0
count=0
while True:
    a = input("Enter a number : ")
    if a == 'Done' or a == 'done':
        break
    value =float(a)
    total=total+value
    count+=1
avg=total/count
print(avg)"""

"""num = list()
while True:
    ip = input("Enter : ")
    if ip == 'Done' or ip == 'done': break
    val = float(ip)
    num.append(val)
avg = sum(num)/len(num)
print(avg)"""


# Strings and List combination
"""a ='ad dd ff'
st =a.split()
print(st)
print(st[1])
for i in st:
    print(i)"""

"""a = 'esjrjj/erg/ttsd/rtr'
st=a.split('/')
print(st)"""

"""a = "from asidejei@gmail.com sat 12.30PM 12-02-22"
word = a.split()
print(word[1])
domain = word[1].split('@')
print(domain[1])"""

