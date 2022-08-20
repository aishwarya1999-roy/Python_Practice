#index of all occurrences of an item in a list in Python

"""list1 = [3, 4, 6, 9, 1, 9]
item = 9
indexes = [i for i in range(len(list1)) if list1[i] == item]
print("Item", item, "is found at index", indexes)"""


# dictionaries
"""
purse = dict()
purse['Money'] = '3' # money -> key, 12 -> value
purse['Tissue'] = 5
purse['Chocolate'] = 8
print(purse)
print(purse['Money'])
purse['Tissue'] = purse['Tissue'] + 5
print(purse)"""

"""dict_1 = {'Aishw' : 1, 'Roy': 23}
print(dict_1)
dict_1['Sept'] = 10
print(dict_1)"""
"""i=0
words = dict()
words['A'] = 1
words['B'] = 1
words['C'] = 1
print(words)
while i<=6:
    words['C']=words["C"]+1
    i=i+1
    print(words)"""

"""count = dict()
list1 = ['Aish', 'Ban', 'Roy']
for name in list1:
    if name not in count:
        count[name]=yes
    else:
        count[name]=count[name]+1
print(count)"""

# how many same words are there in a list using dictionary
"""count = dict()
list1 = ['Ash', 'Ban', 'Roy', 'Ash', 'Ban', 'Roy', 'Roy', 'Ban', 'Roy']
for name in list1:
    if name not in count:
        count[name] = 1
    else:
        count[name] = count[name] + 1
print(count)"""

# Simpler than above
"""count = dict()
list1 = ['Ash', 'Ban', 'Roy', 'Ash', 'Ban', 'Roy', 'Roy', 'Ban', 'Roy']
for name in list1:
    count[name] = count.get(name, 0) + 1
print(count)"""


"""count = dict()
line = input('Enter a line : ')
words = line.split()
print('Words : ', words)
for word in words:
    count[word]= count.get(word, 0) +1
    if count[word]> 1:
        print(word, ' : ', count[word])
print('counts : ', count)"""

"""jjj = {'aish': 10, 'Roy': 30,'aish': 10}

key = list(jjj.keys())
val = list(jjj.values())

d = max(jjj.values())
pos = val.index(d)
print(pos)
print(d, ' : ', key[pos])"""



#dictionary position
"""my_dict ={"java":100, "python":112, "c":11}

# list out keys and values separately
key_list = list(my_dict.keys())
val_list = list(my_dict.values())
print(key_list, val_list)

# print key with val 11
position = val_list.index(11)
print(position, ":",key_list[position])"""

#occurance of a word in a string
"""count = dict()
line = input('Enter a line : ')
words = line.split()
for word in words:
    count[word]= count.get(word, 0) +1
key=list(count.keys())
val = list((count.values()))
d = max(count.values())
pos = val.index(d)
print(key[pos], ' : ',d )"""

#get function
"""stuff = dict()
print(stuff.get('candy', -1))"""