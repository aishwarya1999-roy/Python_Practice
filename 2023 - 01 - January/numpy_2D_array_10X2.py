#Represent the data in a 10x2 array

import numpy as np
days = np.array([1,2,3,4,5,6,7,8,9,10])
steps = np.array([6012, 7079, 6886, 7230, 4598, 5564, 6971, 7763, 8032, 9569])
step_count = np.column_stack([days, steps])
print(step_count)

print("\n \n")

#Perform an appropriate operation on your array to add 2000 steps to all the observations.
additional = [2000]
steps+=additional
print(steps)

print("\n \n")

#Write a program that returns the steps walked if the steps walked are more than 9000.
x = np.where(steps>9000)
print(steps[x])

print("\n \n")

#Print an array containing steps walked in sorted order.
steps.sort()
print(steps)


