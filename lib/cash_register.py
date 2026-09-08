#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        # Validate discount input
        if isinstance(discount, int) and 0 <= discount <= 100:
            self.discount = discount
        else:
            print("Not valid discount")
            self.discount = 0

        self.total = 0
        self.items = []  # flat list of item names
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            self._discount = 0

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity

        # Add item names to items list
        for _ in range(quantity):
            self.items.append(item)

        # Keep full transaction details separately
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            # Match test expectation
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.previous_transactions:
            last_transaction = self.previous_transactions.pop()
            self.total -= last_transaction["price"] * last_transaction["quantity"]

            # Remove item names from items list
            for _ in range(last_transaction["quantity"]):
                if last_transaction["item"] in self.items:
                    self.items.remove(last_transaction["item"])

            print(f"Voided last transaction: {last_transaction}")
        else:
            print("No transactions to void.")
