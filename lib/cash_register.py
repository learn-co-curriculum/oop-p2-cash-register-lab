#!/usr/bin/env python3

  class CashRegister:

    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction = 0

    def add_item(self, item_name, item_price, quantity=1):
        price = item_price * quantity
        self.total += price
        self.last_transaction = price

        for _ in range(quantity):
            self.items.append(item_name)

    def apply_discount(self):
        if self.discount:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction
        self.last_transaction = 0
