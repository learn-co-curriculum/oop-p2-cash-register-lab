#!/usr/bin/env python3

class CashRegister:

    def __init__(self, discount=0):
        # Allow user to input discount, default to 0
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        # Ensure discount is an integer between 0 and 100
        if not isinstance(value, int) or not (0 <= value <= 100):
            print("Not valid discount")
        else:
            self._discount = value

    def add_item(self, item, price, quantity=1):
        # Add total price to running total
        self.total += price * quantity
        # Add item name to items list
        self.items.append(item)
        # Record transaction details
        self.previous_transactions.append({
            "item": item,
            "price": price * quantity,
            "quantity": quantity
        })

    def apply_discount(self):
        # Check if there is a discount to apply
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return
        # Apply discount percentage to total
        self.total = self.total * (1 - self.discount / 100)

    def void_last_transaction(self):
        # Check if there are any transactions to void
        if not self.previous_transactions:
            print("There are no transactions to void.")
            return
        # Remove last transaction and subtract its price from total
        last = self.previous_transactions.pop()
        self.total -= last["price"]
        self.items.remove(last["item"])
