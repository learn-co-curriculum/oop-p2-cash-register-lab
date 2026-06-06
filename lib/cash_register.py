#!/usr/bin/env python3
class CashRegister:

    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity

        for _ in range(quantity):
            self.items.append(title)

        self.previous_transactions.append({
            "title": title,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        self.total = self.total - (
            self.total * self.discount / 100
        )

        if self.total == int(self.total):
            self.total = int(self.total)

        print(
            f"After the discount, the total comes to ${self.total}."
        )

    def void_last_transaction(self):
        if len(self.previous_transactions) == 0:
            return

        last_transaction = self.previous_transactions.pop()

        self.total -= (
            last_transaction["price"] *
            last_transaction["quantity"]
        )

        for _ in range(last_transaction["quantity"]):
            self.items.pop()
