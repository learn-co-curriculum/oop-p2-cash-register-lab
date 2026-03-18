#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        # Validate discount
        if not isinstance(discount, int) or not (0 <= discount <= 100):
            print("Not valid discount")
            self.discount = 0
        else:
            self.discount = discount

        self.total = 0
        self.items = []
        self.previous_transactions = []

    # ---------------------------
    # add_item
    # ---------------------------
    def add_item(self, item, price, quantity=1):
        # Update total
        self.total += price * quantity

        # Add items (including multiples)
        for _ in range(quantity):
            self.items.append(item)

        # Save transaction
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    # ---------------------------
    # apply_discount
    # ---------------------------
    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        discount_amount = (self.discount / 100) * self.total
        self.total -= discount_amount

        print(f"After the discount, the total comes to {self.total}")

    # ---------------------------
    # void_last_transaction
    # ---------------------------
    def void_last_transaction(self):
        if not self.previous_transactions:
            return

        last = self.previous_transactions.pop()

        # Subtract from total
        self.total -= last["price"] * last["quantity"]

        # Remove items (handle multiples)
        for _ in range(last["quantity"]):
            if last["item"] in self.items:
                self.items.remove(last["item"])

        # Ensure total doesn't go negative
        if self.total < 0:
            self.total = 0.0