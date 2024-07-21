import heapq
def minCost(arr,n) :
    heapq.heapify(arr)
    
    total_cost = 0
    while n > 1:
        first = heapq.heappop(arr)
        second = heapq.heappop(arr)
        print(first, second)
        cost = first + second
        total_cost += cost
        heapq.heappush(arr, cost)
        n=n-1

    return total_cost

arr = [4, 3, 2, 6] # 2, 3, 4, 6
N = 4
print(minCost(arr,N))