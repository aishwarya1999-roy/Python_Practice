#Given a list of integer values. Write a python program to check whether it contains same number in adjacent position.
# Display the count of such adjacent occurrences

def get_count(num_list):
    count = 0
    for i in range(0, len(num_list) - 1):
        if num_list[i] == num_list[i + 1]:
            count += 1
    return count
num_list = [1, 1, 5, 100,100, -20, -20, 6, 0, 0]
print(get_count(num_list))


# without function
"""
list1 = [1,2,2,3,4,4,4,10]
count = 0
for i in range(0, len(list1)-1):
    if list1[i] == list1[i + 1]:
        count += 1
print(count)
"""