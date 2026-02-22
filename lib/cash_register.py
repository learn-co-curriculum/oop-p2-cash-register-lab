#!/usr/bin/env python3

class CashRegister:
    """A simple cash register class that tracks transactions and applies discounts."""
    
    def __init__(self, discount=0):
        """
        Initialize a CashRegister instance.
        
        Args:
            discount (int): Optional discount percentage (0-100, default 0)
        """
        self._discount = 0
        self.discount = discount  # Use property setter for validation
        self.total = 0
        self.items = []
        self.previous_transactions = []
    
    @property
    def discount(self):
        """Get the current discount percentage."""
        return self._discount
    
    @discount.setter
    def discount(self, value):
        """
        Set the discount percentage with validation.
        
        Args:
            value (int): Discount percentage to set (must be 0-100)
            
        Prints error message if value is invalid and doesn't change the discount.
        """
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
    
    def add_item(self, item, price, quantity=1):
        """
        Add items to the cash register.
        
        Args:
            item (str): Item name
            price (float): Price per item
            quantity (int): Number of items to add (default 1)
        """
        # Calculate total cost and update register total
        item_total = price * quantity
        self.total += item_total
        
        # Add items to items list quantity times
        self.items.extend([item] * quantity)
        
        # Add transaction to previous_transactions list
        self.previous_transactions.append({
            'item': item,
            'price': price,
            'quantity': quantity
        })
    
    def apply_discount(self):
        """
        Apply discount to the total if discount > 0 and there are transactions.
        
        Prints appropriate message indicating success or that discount can't be applied.
        """
        if self.discount > 0 and self.previous_transactions:
            discount_amount = (self.discount / 100) * self.total
            self.total = int(self.total - discount_amount)  # Tests expect integer result
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")
    
    def void_last_transaction(self):
        """
        Remove the last transaction from the cash register.
        
        Subtracts the transaction's total from the register total and removes items from items list.
        """
        if self.previous_transactions:
            last_transaction = self.previous_transactions.pop()
            transaction_total = last_transaction['price'] * last_transaction['quantity']
            self.total -= transaction_total
            
            # Remove the last transaction's items from items list
            # Remove from the end of the list
            del self.items[-last_transaction['quantity']:]
