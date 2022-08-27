# highest occurence of a word in a file

name = input("Enter a file : ")
handle = open(name)
# print(handle.read())
counts = dict()
for line in handle :
    words = line.split()
    for word in words :
        counts[word] = counts.get(word, 0) + 1
#print(counts)
bigcount = 0
bigword = 0
for word, count in counts.items() :
    if bigcount == 0 or count > bigcount :
        bigword = word
        bigcount = count
print(bigword, ':', bigcount)
