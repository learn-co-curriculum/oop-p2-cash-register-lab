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
        if not isinstance(value, int) or value < 0 or value > 100:
            print("Not valid discount")
            self._discount = 0
            return
        self._discount = value

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(item)
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity,
        })

    def apply_discount(self):
        if not self.previous_transactions or self.discount == 0:
            print("There is no discount to apply.")
            return

        discount_multiplier = 1 - self.discount / 100
        self.total = self.total * discount_multiplier

        if self.total == int(self.total):
            self.total = int(self.total)

        print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            return

        last_transaction = self.previous_transactions.pop()
        amount_to_subtract = last_transaction["price"] * last_transaction["quantity"]
        self.total -= amount_to_subtract
        if self.total == 0:
            self.total = 0

        for _ in range(last_transaction["quantity"]):
            if last_transaction["item"] in self.items:
                self.items.remove(last_transaction["item"])
