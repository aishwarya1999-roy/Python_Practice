# find index of all occurrences of an item in a file in python
name = input('Enter name of a File : ')
handle = open(name, 'r')
count = 0
for line in handle:
    words = line.split()
    print(words)

search = input("Enter element for search : ")
for i in range(len(words)):
    if words[i] == search:
        count += 1
indexes = [i for i in range(len(words)) if words[i] == search]
print(search, "- is is", count, "times in the list. The indexes of the item is", indexes)
handle.close()