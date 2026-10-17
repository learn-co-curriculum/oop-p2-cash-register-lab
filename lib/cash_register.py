
#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.previous_transactions = []
        self.discount = discount

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if (
            isinstance(value, int)
            and not isinstance(value, bool)
            and 0 <= value <= 100
        ):
            self._discount = value
        else:
            print("Not valid discount")
            self._discount = getattr(self, "_discount", 0)

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity

        for _ in range(quantity):
            self.items.append(item)

        transaction = {
            "item": item,
            "price": price,
            "quantity": quantity
        }

        self.previous_transactions.append(transaction)

    def apply_discount(self):
        if not self.previous_transactions or self.discount == 0:
            print("There is no discount to apply.")
            return

        self.total *= (100 - self.discount) / 100

        print(
            f"After the discount, the total comes to ${self.total:g}."
        )

    def void_last_transaction(self):
        if not self.previous_transactions:
            return

        transaction = self.previous_transactions.pop()

        item = transaction["item"]
        price = transaction["price"]
        quantity = transaction["quantity"]

        self.total -= price * quantity

        for _ in range(quantity):
            self.items.remove(item)

        if abs(self.total) < 1e-9:
            self.total = 0.0
