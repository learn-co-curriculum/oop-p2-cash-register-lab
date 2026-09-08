#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        # Use a simple attribute for discount (defaults to 0)
        self.discount = discount
        self.total = 0
        self.items = []
        # previous_transactions stores the numeric total for each add_item call
        self.previous_transactions = []

    def add_item(self, title, price, quantity=1):
        """Add an item to the register. Quantity is optional (default 1)."""
        for _ in range(quantity):
            self.items.append(title)
        transaction_total = price * quantity
        self.total += transaction_total
        self.previous_transactions.append(transaction_total)

    def apply_discount(self):
        """Apply the percentage discount to the total and print a message.

        If no discount was set (0), print an error message instead.
        """
        if not self.discount:
            print("There is no discount to apply.")
            return

        new_total = self.total * (100 - self.discount) / 100
        if new_total == int(new_total):
            new_total = int(new_total)
        self.total = new_total
        print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        """Remove the last transaction amount from the total and history."""
        if not self.previous_transactions:
            return
        last = self.previous_transactions.pop()
        self.total -= last
