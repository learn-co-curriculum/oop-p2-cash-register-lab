#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        """Initialize a cash register with optional discount (percentage)"""
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []
    
    def add_item(self, title, price, quantity=1):
        """
        Add an item to the cash register.
        
        Args:
            title: Name of the item
            price: Price per unit
            quantity: Number of items (default 1)
        """
        # Add the item to items list 'quantity' times
        for _ in range(quantity):
            self.items.append(title)
        
        # Calculate transaction total
        transaction_total = price * quantity
        
        # Add to total
        self.total += transaction_total
        
        # Store transaction for potential voiding
        self.previous_transactions.append({
            "title": title,
            "price": price,
            "quantity": quantity,
            "total": transaction_total
        })
    
    def apply_discount(self):
        """
        Apply the discount to the total price.
        Prints a success message or error message if no discount exists.
        """
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            # Calculate discounted total
            discount_amount = self.total * (self.discount / 100)
            self.total = self.total - discount_amount
            print(f"After the discount, the total comes to ${self.total:.0f}.")
    
    def void_last_transaction(self):
        """
        Remove the last transaction from the register.
        Subtracts the item's price from total and removes it from items list.
        """
        if self.previous_transactions:
            # Get the last transaction
            last_transaction = self.previous_transactions.pop()
            
            # Subtract from total
            self.total -= last_transaction["total"]
            
            # Remove items from items list (quantity times)
            for _ in range(last_transaction["quantity"]):
                self.items.remove(last_transaction["title"])
