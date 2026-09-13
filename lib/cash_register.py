#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.previous_transactions = []
        self._discount = 0  # safe default before validation runs below
        self.discount = discount

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        if isinstance(discount, int) and 0 <= discount <= 100:
            self._discount = discount
        else:
            print("Not valid discount")

    def add_item(self, title, price, quantity=1):
        # add the price (times quantity) to the running total
        self.total += price * quantity

        # record one entry per unit purchased
        self.items += [title] * quantity

        # remember this transaction so it can be voided later
        self.previous_transactions.append({
            "item": title,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        # a register with no discount configured has nothing to apply
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        discount_amount = self.total * self.discount / 100
        self.total -= discount_amount

        # show whole numbers without a trailing .0
        if self.total == int(self.total):
            display_total = int(self.total)
        else:
            display_total = round(self.total, 2)

        print(f"After the discount, the total comes to ${display_total}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            return

        last_transaction = self.previous_transactions.pop()
        title = last_transaction["item"]
        price = last_transaction["price"]
        quantity = last_transaction["quantity"]

        # undo the total this transaction added
        self.total -= price * quantity

        # remove the units this transaction added, starting from
        # the end of the list so we undo the most recent additions
        for _ in range(quantity):
            for index in range(len(self.items) - 1, -1, -1):
                if self.items[index] == title:
                    del self.items[index]
                    break