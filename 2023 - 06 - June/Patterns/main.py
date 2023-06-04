#*
#**
#***
#****
#*****

"""c = []
for i in range(0,5):
    c.append('*')
    print(''.join(c))"""

c = []
for i in range(5, 0, -1):
    c.append('*' * i)
    print(''.join(c))