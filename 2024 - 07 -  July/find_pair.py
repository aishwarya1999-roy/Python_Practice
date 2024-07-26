A = [1, 2,3, 9]

m = 10

n= len(A)
for i in range(0, n-1):
    for j in range(i+1, n-1):
        if i+j == m:
            print(i, j)