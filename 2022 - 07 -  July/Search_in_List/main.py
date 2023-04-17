found = 0
i = 0
x = input("Number to search : ")
xx = float(x)
list1 = [10, 55, 23, 69, 48.32, 100, 80, 110.90]

for j in list1:
    if j == xx:
        found = 1
        break
    else:
        found = 0
    i = i + 1
if found == 1:
    print("Found", j, "at location :", i+1)

elif found == 0:
    print("\nError!! \nNumber not found!")

