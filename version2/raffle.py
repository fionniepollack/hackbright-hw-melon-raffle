"""Randomly pick customer and print customer info"""

# Add code starting here

# Hint: remember to import any functions you need from
# other files or libraries

from random import choice

import customers as cust

def pick_winner(customers):
    """Choose a random winner from list of customers."""

    chosen_customer = choice(customers)

    print("Tell {name} at {email} that they've won".format(
        name=chosen_customer.name,
        email=chosen_customer.email
        ))


def run_raffle():
    """Run the weekly raffle."""

    customers = cust.get_customers_from_file("customers.txt")
    pick_winner(customers)

# executes when file is run directly from CLI
# does NOT execute when imported as a module
if __name__ == '__main__': 
    run_raffle()