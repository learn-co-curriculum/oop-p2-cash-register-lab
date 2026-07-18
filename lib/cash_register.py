#!/usr/bin/env python3


class CashRegister:
    def __init__(self, discount=0):
        self._discount = 0
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

    def add_item(self, item, price, quantity=1):
        # Update total
        self.total += price * quantity

        # Add items to list
        for _ in range(quantity):
            self.items.append(item)

        # Save transaction
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        self.total = self.total * (100 - self.discount) / 100

        # Remove unnecessary .0 when total is a whole number
        if self.total == int(self.total):
            total_display = int(self.total)
        else:
            total_display = self.total

        print(f"After the discount, the total comes to ${total_display}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        last = self.previous_transactions.pop()

        self.total -= last["price"] * last["quantity"]

        for _ in range(last["quantity"]):
            self.items.remove(last["item"])
