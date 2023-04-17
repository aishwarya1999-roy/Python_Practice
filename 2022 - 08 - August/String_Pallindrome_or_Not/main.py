# Write a function, check_palindrome() to check whether the given string is a palindrome or not.
# The function should return true if it is a palindrome else it should return false.
# Note: Initialize the string with various values and test your program.
# Assume that all the letters in the given string are all of the same case.

def check_palindrome(word):
    rev = word[::-1]
    if word == rev:
        return True
    else:
        return False

status=check_palindrome("civic")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")