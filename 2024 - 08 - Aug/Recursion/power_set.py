# def power_set(arr):
#     power = [[]]
#     for num in arr:
#         power += [i + [num] for i in power]
#     return power

# arr = [1,2,3]
# print(power_set(arr))

# def power_set(input_list, ind=0, current_subset=None):
#     if current_subset is None:
#         current_subset = []
#     if ind == len(input_list):
#         return [current_subset]
    
#     subsets_excluding_current = power_set(input_list, ind + 1, current_subset)
#     subsets_including_current = power_set(input_list, ind + 1, current_subset + [input_list[ind]])
    
#     return subsets_excluding_current + subsets_including_current
# # Example usage:
# input_list = [1, 2, 3]
# result = power_set(input_list)
# print(result)


# def power_set(arr1,output,ind,ans):
#     if ind>=len(arr1):
#         ans.append(output[:])
#         return
#     #exclude
#     power_set(arr1,output,ind+1, ans)
#     #include
#     output.append(arr1[ind])
#     power_set(arr1,output,ind+1, ans)
#     output.pop()
# arr1 = [1,2,3]
# ans = []
# power_set(arr1,[],0,ans)
# print(ans)


original_list = [1, 2, 3]
copy_list = original_list[:]  # This creates a shallow copy

# Modify the copy
copy_list.append(4)

print("Original List:", original_list)  # Output: [1, 2, 3]
print("Copy List:", copy_list)          # Output: [1, 2, 3, 4]




