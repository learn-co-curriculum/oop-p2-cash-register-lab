#!/usr/bin/env python3

class CashRegister:
    """
    A cash register that tracks items, totals, and transaction history.
    """

    def __init__(self, discount=0):
        """Initialize the cash register with an optional discount percentage."""
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
        """Add an item to the register and update the total."""
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(item)
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        """Apply the discount percentage to the current total."""
        if self.discount == 0:
            print("There is no discount to apply.")
            return
        self.total = self.total - (self.total * (self.discount / 100))
        print(f"After the discount, the total comes to ${self.total:.0f}.")

    def void_last_transaction(self):
        """Undo the most recent transaction."""
        if not self.previous_transactions:
            return
        last = self.previous_transactions.pop()
        self.total -= last["price"] * last["quantity"]
        for _ in range(last["quantity"]):
            self.items.remove(last["item"])