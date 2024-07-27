# Google mock interview

#Given a set of numbers, find a pair of numbers that add upto a certain target, 
# ex [1, 2, 3, 9] ,and taregt 10, identify that 1 & 9 add upto 10.


#Brute force approch = O(n^2)
"""A = [1, 2, 3, 9]

m = 10

n= len(A)
for i in range(n):
    for j in range(i+1,n):
        if A[i]+A[j] == m:
                print(A[i], A[j])"""

#Using Hash set = O(n)
def find_pair(A, m):
    seen  = set()
    for num in A:
        complement = m - num
        if complement in seen:
            print(num, complement)
            return  # Return after finding the first pair
        seen.add(num)
        

A = [1, 2, 3, 9]
m = 10
find_pair(A, m)