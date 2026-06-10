class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, title, price, quantity=None):
        if quantity is None:
            quantity = 1

        self.total += price * quantity

        for _ in range(quantity):
            self.items.append(title)

        self.previous_transactions.append({
            "title": title,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        self.total = self.total - (self.total * self.discount / 100)
        self.total = round(self.total, 2)

        print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            return

        last = self.previous_transactions.pop()

        self.total -= last["price"] * last["quantity"]

        for _ in range(last["quantity"]):
            if last["title"] in self.items:
                self.items.remove(last["title"])