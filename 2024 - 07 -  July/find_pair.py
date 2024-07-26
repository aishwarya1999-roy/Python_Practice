A = [1, 2, 3, 9]

m = 10

n= len(A)
for i in range(n):
    for j in range(n):
        if A[i]+A[j] == m:
            print(A[i], A[j], "sum = ", A[i]+A[j])

