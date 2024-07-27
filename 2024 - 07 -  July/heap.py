import heapq

arr = [4, 3, 2, 1, 6, 7, 1]

heapq.heapify(arr)

print(arr)

print(heapq.heappop(arr))
print(arr)
heapq.heappush(arr, 1)
print(arr)

heapq._heapify_max(arr)
print(arr)
print(heapq._heappop_max(arr))
print(arr)