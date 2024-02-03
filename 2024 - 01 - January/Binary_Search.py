list1 = [3,6,8,12,14,17,25,29,31,36,42,47,53,55,62]
l = 1
h = len(list1)
key = 42
print(l,h)
mid = int((l+h)/2)
print(mid , " : ", list1[mid])

while True:
    if list1[mid] == key:
        print(f"Found at {mid}")
        break
    elif list1[mid] < key :
        l = mid + 1
    elif list1[mid] > key :
        h = mid - 1
