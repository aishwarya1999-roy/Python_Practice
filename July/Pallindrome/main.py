# Pallindrome opr not

def palindrome(a):
    mid = (len(a) - 1) / 2
    start = 0
    last = len(a) - 1
    flag = 0
    while start <= mid:
        if a[start] == a[last]:
            start += 1
            last -= 1
        else:
            flag = 1
            break
    if flag == 0:
        print("Palindrome!")
    else:
        print("Not Palindrome!")
string = "ahdahd"
palindrome(string)




# Using String Slicing

"""string = "ahdahd"
length = len(string)
half = int(length / 2)

if length % 2 == 0:
    first = string[:half]
    second_half = string[half:]
else:
    first = string[:half]
    second_half = string[half + 1:]

reverse = second_half[::-1]

if first == reverse:
    print("Palindrome!")
else:
    print("Not Palindrome!")"""