name = input("Enter file: ")
if len(name) < 1:
    name = 'text.txt'
handle = open(name)
count = dict()
for line in handle:
    line = line.strip()
    if not line.startswith('From '):
        continue
    words = line.split()
    d = words[5].split(':')

    list1 = list()
    list1.append(d[0])
    for wd in list1:
        count[wd] = count.get(wd, 0) + 1
sor = sorted(count.items())
for k, v in sor:
    print(k, v)

# In python 4 and 04 is different in size, like 4 is bigger than 10 but 04 is smaller than 10, because interpreter
# compares char by char. Like if it is 3>10 : True because 3 is bigger than 1, and if it is 03>10 : False,
# because 0 is smaller than 1
