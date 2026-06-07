# cash_register.py
# This module defines the CashRegister class.
# It models a cash register that can add items, apply discounts,
# and void previous transactions.


class CashRegister:
    """Represents a cash register with discount, total, items, and transaction history."""

    def __init__(self, discount=0):
        # discount is a percentage off the total (e.g. 20 means 20% off)
        self.discount = discount
        # total price of all items added
        self.total = 0
        # list of item names added to the register
        self.items = []
        # list of previous transactions as dicts with item, price, quantity
        self.previous_transactions = []

    # --- Properties ---

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        # Ensure discount is an integer and between 0 and 100 inclusive
        if not isinstance(value, int) or value < 0 or value > 100:
            print("Not valid discount")
        else:
            self._discount = value

    # --- Methods ---

    def add_item(self, item, price, quantity=1):
        """Adds an item to the register.

        Args:
            item (str): The name of the item.
            price (float): The price of a single item.
            quantity (int): The number of items (default is 1).
        """
        # Add the total price of this item to the running total
        self.total += price * quantity

        # Add the item name to the items list (once per quantity)
        for _ in range(quantity):
            self.items.append(item)

        # Record the transaction
        self.previous_transactions.append({
            "item": item,
            "price": price * quantity,
            "quantity": quantity
        })

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            self.total = self.total * (1 - self.discount / 100)
            print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        """Removes the last transaction from the register.
        
        Adjusts the total and items list to reflect the removal.
        """
        if not self.previous_transactions:
            print("There are no transactions to void.")
        else:
            # Get the last transaction
            last = self.previous_transactions.pop()

            # Subtract its price from the total
            self.total -= last["price"]

            # Remove the item(s) from the items list
            for _ in range(last["quantity"]):
                if last["item"] in self.items:
                    self.items.remove(last["item"])

    def __repr__(self):
        return (f"CashRegister(discount={self.discount}, "
                f"total={self.total}, items={self.items})")