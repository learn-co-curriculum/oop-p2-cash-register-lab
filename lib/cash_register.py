#!/usr/bin/env python3

class CashRegister:

    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.previous_transactions = []

      
        self._discount = 0
        self.discount = discount  

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        # Must be a whole number between 0 and 100 inclusive
        if isinstance(discount, int) and 0 <= discount <= 100:
            self._discount = discount
        else:
            print("Not valid discount")    

    def add_item(self, item, price, quantity=1):
        total_price = price * quantity
        self.total += total_price
        for _ in range(quantity):
            self.items.append(item)
        self.previous_transactions.append({
            "item": item,
            "price": total_price,
            "quantity": quantity
    })

    def apply_discount(self):
        if self.previous_transactions:
            discount_amount = self.total * self.discount // 100
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")
    
    def void_last_transaction(self):
        if self.previous_transactions:
            last_transaction = self.previous_transactions.pop()
            self.total -= last_transaction["price"]
            self.items.remove(last_transaction["item"])
        else:
            return "There is no transaction to void."
