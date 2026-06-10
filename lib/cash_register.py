class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity

        for _ in range(quantity):
            self.items.append(title)

        self.last_transaction_amount = price * quantity

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            self.total -= self.total * (self.discount / 100)

            if self.total == int(self.total):
                print(
                    f"After the discount, the total comes to ${int(self.total)}."
                )
            else:
                print(
                    f"After the discount, the total comes to ${self.total}."
                )

    def void_last_transaction(self):
        self.total -= self.last_transaction_amount
        self.last_transaction_amount = 0
