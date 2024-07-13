def max_meet(arr):
    count = 0
    """for i in range(0,len(arr)):
        if arr[i]"""
    return count


start_time = [3, 1, 8, 5, 0, 5]
end_time = [ 4, 2, 9, 7, 6, 9]
# [(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]
sorted_pairs = sorted(zip(start_time, end_time), key=lambda x: x[1])
print(sorted_pairs[1][1])

print(max_meet(sorted_pairs))

