def sumofdigit(n):
    sum_of_digit = 0
    l = str(n)
    for i in l:
        sum_of_digit = sum_of_digit + int(i)
    return sum_of_digit
sum_of_digit = sumofdigit(123)
print(sum_of_digit)
