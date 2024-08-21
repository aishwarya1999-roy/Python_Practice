# def power_set(arr):
#     power = [[]]
#     for num in arr:
#         power += [i + [num] for i in power]
#     return power

# arr = [1,2,3]
# print(power_set(arr))

def power_set(input_list, ind=0, current_subset=None):
    if current_subset is None:
        current_subset = []
    if ind == len(input_list):
        return [current_subset]
    
    subsets_excluding_current = power_set(input_list, ind + 1, current_subset)
    subsets_including_current = power_set(input_list, ind + 1, current_subset + [input_list[ind]])
    
    return subsets_excluding_current + subsets_including_current
# Example usage:
input_list = [1, 2, 3]
result = power_set(input_list)
print(result)
