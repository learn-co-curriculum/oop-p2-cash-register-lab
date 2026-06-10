#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        # Ensure discount is valid integer between 0 and 100
        if not isinstance(discount, int) or discount < 0 or discount > 100:
            print("Not valid discount")
            self.discount = 0
        else:
            self.discount = discount

        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity

        for _ in range(quantity):
            self.items.append(item)

        # Store transaction (one entry per add_item call)
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        self.total = self.total * (1 - self.discount / 100)

        print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        if len(self.previous_transactions) == 0:
            return

        last = self.previous_transactions.pop()

        # Reverse its effect on total
        self.total -= last["price"] * last["quantity"]

        # Remove item from items list if it exists
        if last["item"] in self.items:
            self.items.remove(last["item"])