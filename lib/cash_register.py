#!/usr/bin/env python3

class CashRegister:
    """
    A model for a cash register that handles adding items, applying discounts,
    and voiding previous transactions.
    """

    def __init__(self, discount=0):
        """
        Initializes the cash register.
        :param discount: Optional percentage discount (0-100). Defaults to 0.
        """
        self.total = 0
        self.items = []
        self.previous_transactions = []
        self.discount = discount

    @property
    def discount(self):
        """Getter for discount."""
        return self._discount

    @discount.setter
    def discount(self, value):
        """
        Setter for discount. Ensures it's an integer between 0 and 100.
        Prints "Not valid discount" if validation fails.
        """
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            if not hasattr(self, '_discount'):
                self._discount = 0

    def add_item(self, item, price, quantity=1):
        """
        Adds an item to the cash register.
        :param item: Name of the item.
        :param price: Price of the item.
        :param quantity: Quantity of the item (defaults to 1).
        """
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(item)
        self.previous_transactions.append({"item": item, "price": price, "quantity": quantity})

    def apply_discount(self):
        """
        Applies the discount percentage to the current total.
        If no transactions exist or discount is 0, prints an error message.
        Otherwise, prints the updated total.
        """
        if not self.previous_transactions or self.discount == 0:
            print("There is no discount to apply.")
        else:
            self.total = self.total * (1 - self.discount / 100)
            print(f"After the discount, the total comes to {f'${self.total:g}'}.")

    def void_last_transaction(self):
        """
        Voids the last recorded transaction.
        Updates the total and items list accordingly.
        If no transactions exist, prints an error message.
        """
        if not self.previous_transactions:
            print("There is no transaction to void.")
        else:
            transaction = self.previous_transactions.pop()
            self.total -= transaction['price'] * transaction['quantity']
            for _ in range(transaction['quantity']):
                if transaction['item'] in self.items:
                    self.items.remove(transaction['item'])
