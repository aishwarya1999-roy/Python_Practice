#print counting - recursion
def counting(num):
    if num == 0:
        return 0
    print(num, end=" ")
    return counting(num-1)
    
num = int(input("Number : ")) #5
print(counting(num)) # 5 4 3 2 1 0


#array is sorted or not

