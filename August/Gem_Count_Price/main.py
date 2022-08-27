#ARS Gems Store sells different varieties of gems to its customers.
#Write a Python program to calculate the bill amount to be paid by a customer based on the list of gems and quantity purchased.
# Any purchase with a total bill amount above Rs.30000 is entitled for 5% discount.
# If any gem required by the customer is not available in the store, then consider total bill amount to be -1.
#Assume that quantity required by the customer for any gem will always be greater than 0.
#Perform case-sensitive comparison wherever applicable.

def calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity):
    bill_amount, total = 0, 0
    i = 0
    check = all(item in gems_list for item in reqd_gems)
    if check is True:
        while i < len(reqd_gems):
            inter = gems_list.index(reqd_gems[i])
            total = total + price_list[inter] * reqd_quantity[i]
            i = i + 1
        if total > 30000:
            bill_amount = total - (total * 0.05)
        else:
            bill_amount = total
    else:
        bill_amount = -1
    return bill_amount
gems_list = ["Emerald", "Ivory", "Jasper", "Ruby", "Garnet"]
price_list = [1760, 2119, 1599, 3920, 3999]
reqd_gems = ["Ivory", "Emerald", "Garnet"]
reqd_quantity = [3, 10, 12]
print(calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity))