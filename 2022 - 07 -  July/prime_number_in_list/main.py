# Prime Numbers in list
def prime(list3):
    for i in list3:
        if i == 0 or i == 1:
            continue
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            list2.append(i)
    return list2
list1 = [7, 9, 11, 13, 15, 20, 23]
list2 = []
print(prime(list1))

