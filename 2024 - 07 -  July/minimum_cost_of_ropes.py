import heapq
def minCost(arr,n) :
    heapq.heapify(arr)
    
    total_cost = 0
    while n > 1:
        first = heapq.heappop(arr)
        second = heapq.heappop(arr)
        cost = first + second
        total_cost += cost
        
        # Insert the new rope back into the heap
        heapq.heappush(arr, cost)

    return first

arr = [4, 3, 2, 6] # 2, 3, 4, 6
N = 4
print(minCost(arr,N))