class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.previous_transactions = []

        # validate discount
        if isinstance(discount, int) and 0 <= discount <= 100:
            self.discount = discount
        else:
            print("Not valid discount")
            self.discount = 0

    # property for discount with validation
    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity):
        # update total
        self.total += price * quantity

        # store item name(s)
        for _ in range(quantity):
            self.items.append(item)

        # record transaction
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return

        # apply discount
        self.total = self.total - (self.total * (self.discount / 100))

        # remove last transaction
        self.previous_transactions.pop()

    def void_last_transaction(self):
        if not self.previous_transactions:
            return

        last = self.previous_transactions.pop()

        # reverse its effect on total
        self.total -= last["price"] * last["quantity"]

        # remove items from list
        item = last["item"]
        quantity = last["quantity"]

        for _ in range(quantity):
            if item in self.items:
                self.items.remove(item)