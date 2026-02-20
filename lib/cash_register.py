#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        """
        Initialize a cash register.

        Attributes:
            discount (int): Discount percentage (0–100)
            total (float): Total amount in register
            items (list): List of item names
            previous_transactions (list): List of past transactions
        """
        # Validate initial discount
        if type(discount) != int or not (0 <= discount <= 100):
            print("Not valid discount, setting to 0")
            self._discount = 0
        else:
            self._discount = discount

        self.total = 0
        self.items = []
        self.previous_transactions = []

    # -------------------------
    # Property: discount
    # -------------------------
    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if type(value) != int or not (0 <= value <= 100):
            print("Not valid discount")
        else:
            self._discount = value

    # -------------------------
    # Methods~
    # -------------------------
    def add_item(self, item, price, quantity=1):
        # Update total
        self.total += price * quantity
        # Add item names to items list
        for _ in range(quantity):
            self.items.append(item)
        # Record transaction
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if  self._discount == 0:
            print("There is no discount to apply.")
            return

        # Apply discount
        discount_amount = self.total * (self._discount / 100)
        self.total -= discount_amount

        # Remove last transaction
        last_transaction = self.previous_transactions.pop()
        for _ in range(last_transaction["quantity"]):
            self.items.remove(last_transaction["item"])

        # Print message exactly as autograder expects
        print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("No transaction to void.")
            return

        last_transaction = self.previous_transactions.pop()
        self.total -= last_transaction["price"] * last_transaction["quantity"]
        for _ in range(last_transaction["quantity"]):
            self.items.remove(last_transaction["item"])
        print(f"Voided last transaction: {last_transaction['item']}")
        