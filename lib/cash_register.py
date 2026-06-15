#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=None):
        
        if discount is None:
            try:
                discount = int(input("Enter discount percentage (0-100): "))
            except ValueError:
                discount = 0

        
        if isinstance(discount, int) and 0 <= discount <= 100:
            self.discount = discount
        else:
            print("Not valid discount")
            self.discount = 0

        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def Discount(self):
        return self.discount

    def add_item(self, item, price, quantity=1):
        cost = price * quantity
        self.total += cost
        self.items.append({"item": item, "price": price, "quantity": quantity})
        self.previous_transactions.append({"item": item, "price": price, "quantity": quantity})
        print(f"Added {quantity} x {item} at {price} each. Total: {self.total}")

    def apply_discount(self):
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return

        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            
            self.previous_transactions.pop()
            print(f"Applied {self.discount}% discount. New total: {self.total}")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("No previous transactions to void.")
            return

        last_transaction = self.previous_transactions.pop()
        cost = last_transaction["price"] * last_transaction["quantity"]
        self.total -= cost
        
        self.items.pop()
        print(f"Voided last transaction: {last_transaction['item']}. New total: {self.total}")
