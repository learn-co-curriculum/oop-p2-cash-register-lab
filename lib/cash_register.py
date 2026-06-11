class CashRegister:
    def __init__(self, discount=0):
        if discount < 0 or discount > 100:
            print("Not valid discount")
            discount = 0

        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity

        # add item multiple times for correct tracking
        for _ in range(quantity):
            self.items.append(item)

        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        discount_amount = (self.discount / 100) * self.total
        self.total -= discount_amount

        print(f"After the discount, the total comes to ${self.total:.0f}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        last = self.previous_transactions.pop()

        self.total -= last["price"] * last["quantity"]

        # remove items correctly (respect quantity)
        for _ in range(last["quantity"]):
            if last["item"] in self.items:
                self.items.remove(last["item"])