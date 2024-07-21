import heapq
def minCost(arr,n) :
    heapq.heapify(arr)
    
    total_cost = 0
    
    # While there is more than one rope
    while n > 1:
        # Extract the two smallest ropes
        first = heapq.heappop(arr)
        second = heapq.heappop(arr)
        
        # Calculate the cost of connecting them
        cost = first + second
        total_cost += cost
        
        # Insert the new rope back into the heap
        heapq.heappush(arr, cost)

    return first

arr = [4, 3, 2, 6] # 2, 3, 4, 6
N = 4
print(minCost(arr,N))