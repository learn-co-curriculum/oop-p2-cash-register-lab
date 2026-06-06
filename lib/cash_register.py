#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        # Initialize instance variables
        self.total = 0
        self.items = []
        self.previous_transactions = []
        
        # Use the property setter to validate the initial discount
        self._discount = 0
        self.discount = discount

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        # Ensure discount is an integer and between 0-100 inclusive
        if type(value) is not int or value < 0 or value > 100:
            print("Not valid discount")
        else:
            self._discount = value

    def add_item(self, title, price, quantity=1):
        # Add price * quantity to total
        self.total += price * quantity
        
        # Add item to the items array 'quantity' times
        for _ in range(quantity):
            self.items.append(title)
            
        # Add an object to previous_transactions to keep track for voiding
        self.previous_transactions.append({
            "title": title,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        # Check if there is a valid discount to apply
        if self.discount > 0:
            # Calculate discount amount and subtract from total
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            
            # Format the total to remove trailing .0 if it's a whole number
            # e.g., 800.0 becomes 800 to match the expected test string exactly
            print(f"After the discount, the total comes to ${self.total:g}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        # Check if there are any transactions to void
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return
            
        # Remove the last transaction record from the array
        last_transaction = self.previous_transactions.pop()
        
        # Subtract the transaction amount from the total
        self.total -= last_transaction["price"] * last_transaction["quantity"]
        
        # Remove the item(s) from the items array
        # Since we always append to the end, popping from the end correctly 
        # removes the exact items added in the last transaction.
        for _ in range(last_transaction["quantity"]):
            self.items.pop()