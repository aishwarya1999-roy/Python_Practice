# decimal_to_binary
def decimal_to_binary(x):
    res = ""
    while x > 0:
        if x%2 == 1:
            res+="1"
        else:
            res+="0"
        x//=2
    return res[::-1]
x = 9
print(decimal_to_binary(x))


# binary_to_decimal

def binary_to_decimal(binary_str):
    decimal_value = 0
    for i, digit in enumerate (reversed (binary_str)):
        if digit == '1':
            decimal_value += 2 ** i
    return decimal_value
binary_string = "1100"
print(binary_to_decimal(binary_string))