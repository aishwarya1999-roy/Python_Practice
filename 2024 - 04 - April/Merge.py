"""A = [1, 5, 6, 7, 9]
B = [3, 4, 8, 10, 12]
m = len(A)
n = len(B)

C = [0] * (m + n)
print(C)
i = 0
j = 0
k = 0

while i <= m - 1 and j <= n - 1:
    if A[i] < B[j]:
        C[k] = A[i]
        i += 1
    else:
        C[k] = B[j]
        j += 1
    k += 1

while i < m:
    C[k] = A[i]
    i += 1
    k += 1

while j < n:
    C[k] = B[j]
    j += 1
    k += 1

print(C)"""

def merge(A,B):
    C = []
    i = j= 0
    while i < len(A) and j <= len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    C.extend(A[i:])
    C.extend(B[j:])
    return C

A = [1, 5, 6, 7, 9]
B = [3, 4, 8, 10, 12]
print(merge(A,B))