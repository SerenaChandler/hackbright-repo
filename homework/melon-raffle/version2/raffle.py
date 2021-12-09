"""Randomly pick customer and print customer info"""

# Add code starting here
import customers
import random
# Hint: remember to import any functions you need from
# other files or libraries
def pick_winner(customers):
    winner = random.choice(customers)

    name = winner.name
    email = winner.email

    print(f"the winner is... {name} at {email}!!!")

def start_raffle():
    customer = customers.get_customers_from_file("customers.txt")
    pick_winner(customer)