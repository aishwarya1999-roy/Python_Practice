def minCost(arr,n) :
    arr.sort()
    sum = arr[0]
    for i in range(n-1):
        sum = sum + arr[i+1]
        print(sum)
    

arr = [4, 3, 2, 6] # 2, 3, 4, 6
N = 4
print(minCost(arr,N))