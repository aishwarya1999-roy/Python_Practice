# Google mock interview

#Given a set of numbers, find a pair of numbers that add upto a certain target, 
# ex [1, 2, 3, 9] ,and taregt 10, identify that 1 & 9 add upto 10.

A = [1, 2, 3, 9]

m = 10

n= len(A)
for i in range(n):
    for j in range(n):
        if A[i]+A[j] == m:
            print(A[i], A[j], "sum = ", A[i]+A[j])

