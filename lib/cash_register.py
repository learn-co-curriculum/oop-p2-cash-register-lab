class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.previous_transactions = []
        self.discount = discount  

    @property
    def discount(self):
        """Return the current discount percentage (0–100)."""
        return getattr(self, "_discount", 0)

    @discount.setter
    def discount(self, value):
        """
        Validate the discount value.
        Accepts only integers between 0 and 100 inclusive.
        If invalid, prints a message and keeps previous value.
        """
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        """
        Add an item to the register.
        - Increase total by (price * quantity)
        - Add item names to items list
        - Store transaction details in previous_transactions
        """
        self.total += price * quantity

        for _ in range(quantity):
            self.items.append(item)

        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        """
        Apply a percentage discount to the total.
        - If discount is 0, print message.
        - Otherwise, subtract the correct discount amount from total.
        - Print message with new total.
        """
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            # calculate how much to subtract
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            self.total = round(self.total, 2)

            # print success message exactly 
            print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        """
        Undo the last transaction.
        - Remove it from previous_transactions
        - Subtract its amount from total
        - Remove matching items from items list
        - If no transactions exist, do nothing
        """
        if not self.previous_transactions:
            return

        # get the last recorded transaction
        last = self.previous_transactions.pop()
        # subtract its total cost
        self.total -= last["price"] * last["quantity"]

        # remove items from the list according to their quantity
        for _ in range(last["quantity"]):
            try:
                self.items.remove(last["item"])
            except ValueError:
                # ignore if item already removed or not found
                break

        # round total to 2 decimals
        self.total = round(self.total, 2)