#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self._discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        # Discount must be a whole number between 0 and 100
        if not isinstance(value, int) or not (0 <= value <= 100):
            print("Not valid discount")
        else:
            self._discount = value

    def add_item(self, item, price, quantity=1):
        # Accumulate total, expand items list, and record transaction
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(item)
        self.previous_transactions.append({"item": item, "price": price, "quantity": quantity})

    def apply_discount(self):
        # Reject if no discount is configured
        if self._discount == 0:
            print("There is no discount to apply.")
            return
        self.total -= self.total * (self._discount / 100)
        print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        # Reject if there is nothing to void
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return
        last = self.previous_transactions.pop()
        self.total -= last["price"] * last["quantity"]
        for _ in range(last["quantity"]):
            self.items.remove(last["item"])
