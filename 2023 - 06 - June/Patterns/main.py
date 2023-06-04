#*
#**
#***
#****
#*****

"""c = []
for i in range(0,5):
    c.append('*')
    print(''.join(c))"""

#*****
#****
#***
#**
#*

"""c = []
for i in range(5, 0, -1):
    c.append('*'*i)
    print(c[-1])"""

#1
#12
#123
#1234
#12345

"""c = []
for i in range(1, 6):
    c.append(str(i))
    print(int(''.join(c)))"""


for i in range(5, 0, -1):
    for j in range(5, 0):
        print(j, end=' ')
    print()
