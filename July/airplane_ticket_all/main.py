# The flight ticket rates for a round-trip (Mumbai->Dubai) were as follows:
# Rate per Adult: Rs. 37550.0
# Rate per Child: 1/3rd of the rate per adult
# Service Tax: 7% of the ticket amount (including all passengers)
# As it was a holiday season, the airline also offered 10% discount on the final ticket cost (after inclusion of the service tax).
# Find and display the total ticket cost for a group which had adults and children.
# Test the program with different input values for number of adults and children.



def calculate_total_ticket_cost(no_of_adults, no_of_children) :
    total_ticket_cost = 0

    rate = 37550.0
    rate_for_child = (rate / 3)

    ticket_cost = (rate * no_of_adults) + (rate_for_child * no_of_children)
    after_service_tax = ticket_cost + ((ticket_cost * 7) / 100)
    total_ticket_cost = after_service_tax - ((after_service_tax * 10) / 100)

    return total_ticket_cost

total_ticket_cost = calculate_total_ticket_cost(5, 2)
print("Total Ticket Cost:", total_ticket_cost)