"""tup1 = (1,2,46,2,650,43,3)
d=tup1.count(tup1)
print(tup1)

(a,b) = (1,3)
print(b)
dic = {'cis' : 10 , 'dis' : 15}
for (i,k) in dic.items():
    print(i,k)
tup = dic.items()
print(tup)
"""

"""if (6,0,0)>(5,1,3):
    print('yes')
else:
    print('No')"""

# sort a dictionary based on keys
"""di = {'A' : 1, 'L' : 4, 'S': 5, 'E' : 3, 'B': 2}
print(di)
o=sorted(di.items())
print(o)
for k,v in o:
    print(k,v)
"""

# sort a dictionary based on values
"""di = {'A' : 1, 'L' : 4, 'S': 5, 'E' : 3, 'B': 2}
d =list()
for k,v in di.items():
    d.append((v,k))
print(d)
d = sorted(d, reverse=True)
print(d)"""

#making a dictionary to a list of tuples
"""c = {'A' : 1, 'L' : 4, 'S': 5, 'E' : 3, 'B': 2}
lis = list()
for k,v in c.items():
    a=(k,v)
    lis.append(a)
print(lis)"""

# this instade of the above
# print([(k,v) for k,v in c.items()])
