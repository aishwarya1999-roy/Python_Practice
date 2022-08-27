# count occurrence of mail id

name = input("Enter file: ")
if len(name) < 1:
    name = 'text.txt'
handle = open(name)

count = dict()
for line in handle:
    line = line.strip()
    if not line.startswith('From'):
        continue
    words = line.split()
    words = words[1]
    count[words]= count.get(words, 0)+1

max_key = 0
max_val = 0

for k,v in count.items():
    if max_val == 0 or v>max_val:
        max_key = k
        max_val = v
print(max_key, max_val)
