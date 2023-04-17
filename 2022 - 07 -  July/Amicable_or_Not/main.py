# check_amicable_numbers

def amicable_or(x, y):
    fact1, fact2 = [], []
    for j in range(1, x):
        if x % j == 0:
            fact1.append(j)
    for j in range(1, y):
        if y % j == 0:
            fact2.append(j)
    if sum(fact1) == y and sum(fact2) == x:
        return True
    else:
        return False
a, b = 220, 284
if amicable_or(a, b):
    print("Numbers are amicable number")
else:
    print("Numbers are Not amicable Number")