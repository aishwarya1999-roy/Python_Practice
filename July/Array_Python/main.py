import array as arr

# creating an array with integer type
a = arr.array('i', [4, 6, 5]) # 'i' for int , 'f' for float, 'd' for double

# printing original array
print("The new created array is : ", end=" ")
for i in range(0,len(a)):
    print(a[i])
a.insert(1, 3) #insert to add
print(a)
a.pop(3) #delete value from the location entered
print(a)
print(a[1:])
