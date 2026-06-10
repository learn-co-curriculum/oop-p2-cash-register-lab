#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount
    
    @discount.setter
    def discount(self, value):
        if not isinstance(value, int):
            print("Not valid discount.")
            return
        if value < 0 or value > 100:
            print("Not valid discount.")
            return
        self._discount = value

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
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
            return
        
        if len(self.previous_transactions) == 0:
            print("There is no discount to apply.")
            return
        
        discount_amount = self.total * (self.discount / 100)
        self.total = self.total - discount_amount
        print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        if len(self.previous_transactions) == 0:
            print("There is no transaction to void.")
            return
        
        last_transaction = self.previous_transactions.pop()
        self.total -= last_transaction["price"] * last_transaction["quantity"]
        self.items.remove(last_transaction["item"])