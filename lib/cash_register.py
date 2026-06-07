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
        if type(value) is int and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        self.total = round(self.total, 2)
        for _ in range(quantity):
            self.items.append(item)
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            self.total -= self.total * (self.discount / 100)
            self.total = round(self.total, 2)
            formatted_total = int(self.total) if self.total % 1 == 0 else self.total
            print(f"After the discount, the total comes to ${formatted_total}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            return
        
        last_transaction = self.previous_transactions.pop()
        item = last_transaction["item"]
        price = last_transaction["price"]
        quantity = last_transaction["quantity"]
        
        self.total -= price * quantity
        self.total = round(self.total, 2)
        
        # Remove the last quantity instances of this item from the items list
        for _ in range(quantity):
            for idx in range(len(self.items) - 1, -1, -1):
                if self.items[idx] == item:
                    self.items.pop(idx)
                    break
