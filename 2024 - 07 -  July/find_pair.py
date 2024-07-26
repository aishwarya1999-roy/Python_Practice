A = [1, 2, 3, 9]

m = 10

n= len(A)
for i in range(0, n-1):
    for j in range(0, n-1):
        if A[i]+A[j] != m:
            print(A[i], A[j], "sum = ", i+j)

