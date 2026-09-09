class CashRegister:
    """A simple cash register that tracks items, totals, discounts and transactions."""
 
    def __init__(self, discount=0):
        # discount goes through the property setter so it gets validated
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []
 
    @property
    def discount(self):
        return self._discount
 
    @discount.setter
    def discount(self, value):
        # must be a whole number percentage between 0 and 100
        # (type() is int rather than isinstance() so True/False are rejected)
        if type(value) is int and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            # fall back to 0 so the object stays usable
            if not hasattr(self, "_discount"):
                self._discount = 0
 
    def add_item(self, item, price, quantity=1):
        """Add an item to the register, updating the total and history."""
        self.total += price * quantity
 
        # one entry in items per unit purchased
        for _ in range(quantity):
            self.items.append(item)
 
        # record the transaction so it can be voided later
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })
 
    def apply_discount(self):
        """Take the discount percentage off the running total."""
        if self.discount > 0:
            self.total -= self.total * self.discount / 100
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")
 
    def void_last_transaction(self):
        """Undo the most recent transaction, restoring total and items."""
        if not self.previous_transactions:
            print("There are no transactions to void.")
            return
 
        last = self.previous_transactions.pop()
 
        # roll the price back off the total
        self.total -= last["price"] * last["quantity"]
 
        # remove the same number of copies from items
        for _ in range(last["quantity"]):
            if last["item"] in self.items:
                self.items.remove(last["item"])
 
        # nothing left means the register is empty
        if not self.previous_transactions:
            self.total = 0