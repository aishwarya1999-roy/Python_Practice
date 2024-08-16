#print digit in string
def say_digit(digits,arr):
    if digits == 0:
        return 
    dig = digits%10
    digits=digits//10
    say_digit(digits, arr)
    print(arr[dig], end=" ")

arr = ['Zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digits = int(input("Digits : ")) #Digits : 456
say_digit(digits, arr) #four five six 