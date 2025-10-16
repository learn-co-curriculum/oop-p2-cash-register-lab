#!/usr/bin/env python3



class CashRegister:
    def __init__(self, discount=0):
        self._discount = 0
        self.total = 0
        self.items = []
        self.previous_transactions = []  
        self.discount = discount  

    
    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if not isinstance(value, int) or not (0 <= value <= 100):
            raise ValueError("Discount must be an integer between 0 and 100.")
        self._discount = value

    
    def add_item(self, title, price, quantity=1):
        qty = quantity if isinstance(quantity, int) and quantity > 0 else 1
        subtotal = price * qty
        self.total += subtotal
        # items list includes multiples
        for _ in range(qty):
            self.items.append(title)
        # for void
        self.previous_transactions.append(subtotal)

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return
        # percentage off current total
        self.total = int(self.total * (100 - self.discount) / 100)
        print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            return
        last = self.previous_transactions.pop()
        self.total -= last
        