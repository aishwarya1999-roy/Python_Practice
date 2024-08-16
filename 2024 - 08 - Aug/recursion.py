#counting - recursion
def counting(num):
    if num == 0:
        return 0
    print(num, end=" ")
    return counting(num-1)
    
num = int(input("Number : "))
print(counting(num))


#array is sorted or not

