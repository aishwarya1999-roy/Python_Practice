def minCost(arr,n) :
    arr.sort()
    sum = 0
    for i in range(n):
        sum = sum + arr[i]
    return arr

arr = [4, 3, 2, 6] # 2, 3, 4, 6
N = 4
print(minCost(arr,N))