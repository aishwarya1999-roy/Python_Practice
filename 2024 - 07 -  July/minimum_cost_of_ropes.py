import heapq
def minCost(arr,n) :
    total_cost = 0
    heapq.heapify(arr)
    return total_cost

arr = [4, 3, 2, 6] # 2, 3, 4, 6
N = 4
print(minCost(arr,N))