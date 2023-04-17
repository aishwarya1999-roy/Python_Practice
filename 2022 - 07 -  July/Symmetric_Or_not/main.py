# Check the string is symmetric or not

def symmetric(a):
    n = len(a)
    flag = 0
    if n % 2:
        mid = n // 2 + 1
    else:
        mid = n // 2
    start1 = 0
    start2 = mid
    while start1 < mid and start2 < n:
        if a[start1] == a[start2]:
            start1 += 1
            start2 += 1
        else:
            flag = 1
            break
    if flag == 0:
        print("String is symmetric!")
    else:
        print("String is not symmetric!")
string = "ahdahd"
symmetric(string)

# using string slicing


"""length = len(string)
half = int(length / 2)

if length % 2 == 0:
    first_half = string[:half]
    second_half = string[half:]
else:
    first_half = string[:half]
    second_half = string[half + 1:]

# symmetric
if first_half == second_half:
    print("Symmetric!")
else:
    print("Not symmetric!")
"""