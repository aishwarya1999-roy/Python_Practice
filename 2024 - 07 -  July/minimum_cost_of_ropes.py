def minCost(arr,n) :
    arr.sort()
    addd = arr[0]
    aa = []
    for i in range(n-1):
        addd = addd + arr[i+1]
        aa.append(addd)

    return sum(aa)

arr = [4, 3, 2, 6] # 2, 3, 4, 6
N = 4
print(minCost(arr,N))