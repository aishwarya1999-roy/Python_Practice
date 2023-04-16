# Binary Search

num = [68, 15, 4, 9, 21, 34, 57, 91]
num.sort()
print(num)

l = len(num)
if l % 2 == 0 :
    print("even")
    mid = (l // 2) - 1
    print(num[mid])
else :
    print("odd")
    mid = l // 2
    print(num[mid])

value = int(input("Which value you want to search : "))


while mid != value :
    if num[mid] == value :
        print("Value found at : ", mid+1)
    elif num[mid] < value :
        i = mid
        mid = (i + len(num)) // 2
        i = i + 1
        continue
    elif num[mid] > value :
        end = mid
        i = 0
        mid = (i + end) // 2
        i = i + 1
        continue
    break