#!/usr/bin/env python3

class CashRegister:
    """
    Represents a cash register for an e-commerce application.
    """

    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            self._discount = 0

    def add_item(self, item, price, quantity=1):
        """
        Add an item to the register.
        """
        self.total += price * quantity

        # Adds the item once for each quantity purchased
        self.items.extend([item] * quantity)

        transaction = {
            "item": item,
            "price": price,
            "quantity": quantity
        }

        self.previous_transactions.append(transaction)

    def apply_discount(self):
        """
        Apply the discount to the total.
        """
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        self.total = self.total * (1 - self.discount / 100)

        # Convert whole-number floats (e.g. 800.0) to integers
        if isinstance(self.total, float) and self.total.is_integer():
            self.total = int(self.total)

        print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        """
        Remove the last transaction.
        """
        if not self.previous_transactions:
            return

        last_transaction = self.previous_transactions.pop()

        self.total -= (
            last_transaction["price"] *
            last_transaction["quantity"]
        )

        # Removes one entry for each quantity
        for _ in range(last_transaction["quantity"]):
            self.items.remove(last_transaction["item"])