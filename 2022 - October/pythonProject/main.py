
sum = int(input("Enter Base Money : "))
day = int(input("Maximum day : "))
i=1
while i<=day:
    sum = sum + ((sum*5)/100)
    i+=1
print("Final Money : ", sum)