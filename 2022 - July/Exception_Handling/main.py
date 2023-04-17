# Exception Handling

"""def calculate_expenditure(list_of_expenditure):
    total = 0
    for expenditure in list_of_expenditure:
        try:
            total += expenditure
        except:
            total = total + int(expenditure)
    print(total)
list_of_values = [100, 200, 300, "400", 500]
calculate_expenditure(list_of_values)"""

# types of exception

# ZeroDivisionError
"""num_list = []
total = 0
avg = total / len(num_list)
"""
# TypeError
'''total = 10
total += "20"'''

# NameError
'''avg=total/10'''

# IndexError
'''num_list = [1, 2, 3, 4]
value = num_list[4]'''

# ValueError
# string is a valid data type for int() but the value “A” is invalid, as "A" can't be converted into int.
"""value = "A"
num = int(value)"""

# exception handling tryout
"""
def calculate_expenditure(list_of_expenditure):
    total = 0
    try:
        for expenditure in list_of_expenditure:
            total += expenditure
        print("Total:", total)
        avg = total / num_values
        print("Average:", avg)
    except ZeroDivisionError:
        print("Divide by Zero error")
    except TypeError:
        print("Wrong data type")
    except: # Default except - it should be in last 
        print("Some error occurred")
list_of_values = [100, 200, 300, "400", 500]
num_values = 0
calculate_expenditure(list_of_values)"""

# exception handling tryout

"""def calculate_sum(list_of_expenditure):
    total = 0
    try:
        for expenditure in list_of_expenditure:
            total += expenditure
        print("Total:", total)
        avg = total / no_values
        print("Average:", avg)
    except ZeroDivisionError:
        print("Divide by Zero error")
    except TypeError:
        print("Wrong data type")
try:
    list_of_values = [100, 200, 300, 400, 500]
    num_values = len(list_of_values)
    calculate_sum(list_of_values)
except NameError:
    print("Name error occurred")
except:
    print("Some error occurred")"""

# Finally : even if the code have exception,a code written inside the finally block will ALWAYS be executed.
"""balance = 1000
amount = "300Rs"
def take_card():
    print("Take the card out of ATM")
try:
    if balance >= int(amount):
        print("Withdraw")
    else:
        print("Invalid amount")
except TypeError:
    print("Type Error Occurred")
except ValueError:
    print("Value Error Occurred")
except:
    print("Some error Occurred")
finally:
    take_card()"""