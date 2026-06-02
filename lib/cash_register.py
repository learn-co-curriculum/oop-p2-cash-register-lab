#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        if not isinstance(discount, int) or discount < 0 or discount > 100:
            print("Not valid discount")
            discount = 0

        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity

        for _ in range(quantity):
            self.items.append(item)

        transaction = {
            "item": item,
            "price": price,
            "quantity": quantity
        }

        self.previous_transactions.append(transaction)

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        discounted_total = int(
            self.total * ((100 - self.discount) / 100)
        )

        self.total = discounted_total

        print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        if len(self.previous_transactions) == 0:
            print("There is no transaction to void.")
            return

        last_transaction = self.previous_transactions.pop()

        item = last_transaction["item"]
        price = last_transaction["price"]
        quantity = last_transaction["quantity"]

        self.total -= price * quantity

        for _ in range(quantity):
            if item in self.items:
                self.items.remove(item)