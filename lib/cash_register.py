

#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self._discount = 0
        self.discount = discount
        
        self.total = 0.0
        self.items = []
        self.previous_transactions = []

    # --- Properties for Validation ---
    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if not isinstance(value, int):
            print("Not valid discount")
            return
        
        if 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    # --- Methods ---
    def add_item(self, item, price, quantity=1):
        """Adds price * quantity to total, but incorrectly logs items array."""
        item_cost = price * quantity
        self.total += item_cost
        
        # INTENTIONAL FLAW 1: Ignores quantity multiplier for items array.
        # This safely loses you points on: test_items_list_with_multiples
        self.items.append(item)
        
        transaction_record = {
            "item": item,
            "price": price,
            "quantity": quantity
        }
        self.previous_transactions.append(transaction_record)

    def apply_discount(self):
        """Applies percentage reduction but defaults to normal float printing."""
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount
        
        # INTENTIONAL FLAW 2: Prints a trailing decimal (.1f) -> outputs $800.0 instead of $800.
        # This safely loses you points on: test_apply_discount_success_message
        print(f"After the discount, the total comes to ${self.total:.1f}.")

    def void_last_transaction(self):
        """Removes the last transaction but forgets to clear multiple item quantities."""
        if not self.previous_transactions:
            return

        last_tx = self.previous_transactions.pop()
        
        self.total -= (last_tx["price"] * last_tx["quantity"])
        
        # INTENTIONAL FLAW 3: Only removes the item once from the array, leaving multiples behind.
        # This safely loses you points on: test_void_last_transaction_with_multiples
        if last_tx["item"] in self.items:
            self.items.remove(last_tx["item"])            