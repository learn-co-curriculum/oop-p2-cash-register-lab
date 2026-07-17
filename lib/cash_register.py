#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        # discount is optional; defaults to 0 (no discount) if not provided
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        # Enforce discount is an integer between 0 and 100 inclusive
        if isinstance(discount, int) and 0 <= discount <= 100:
            self._discount = discount
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        # Adds the item's total cost (price * quantity) to the running total
        self.total += price * quantity
        # Records each unit of the item individually in the items list
        for _ in range(quantity):
            self.items.append(item)
        # Logs this transaction so it can later be voided or referenced
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        # No discount set on this register means there's nothing to apply
        if self.discount == 0:
            print("There is no discount to apply.")
            return
        # Reduce total by the discount percentage
        self.total -= self.total * (self.discount / 100)
        # Format cleanly so whole numbers don't show a trailing ".0"
        print(f"After the discount, the total comes to ${self.total:g}.")

    def void_last_transaction(self):
        # Nothing to void if no transactions have been recorded
        if not self.previous_transactions:
            return
        # Remove the most recent transaction and reverse its effect on total
        last_transaction = self.previous_transactions.pop()
        self.total -= last_transaction["price"] * last_transaction["quantity"]
        # Remove the corresponding item entries from the items list
        for _ in range(last_transaction["quantity"]):
            if last_transaction["item"] in self.items:
                self.items.remove(last_transaction["item"])