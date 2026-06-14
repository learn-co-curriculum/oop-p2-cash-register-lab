class CashRegister:
    def __init__(self, discount=0):
        # Use the setter property to validate the initial discount value
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    # --- Properties for Validation ---
    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        # Ensure discount is an integer and between 0-100 inclusive
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            self._discount = 0  # Default fallback if validation fails

    # --- Methods ---
    def add_item(self, item, price, quantity):
        line_total = price * quantity
        self.total += line_total
        
        # Add item name to items array
        self.items.append(item)
        
        # Add a dictionary representation to previous_transactions
        transaction_record = {
            "item": item,
            "price": price,
            "quantity": quantity
        }
        self.previous_transactions.append(transaction_record)

    def apply_discount(self):
        if self.total > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            return self.total
        else:
            print("Total is 0, no discount applied.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        # Remove the last item recorded
        last_transaction = self.previous_transactions.pop()
        
        # Reclaim the cost from the total
        deduction = last_transaction["price"] * last_transaction["quantity"]
        self.total -= deduction
        
        # Remove from the main items list if it's there
        if last_transaction["item"] in self.items:
            self.items.remove(last_transaction["item"])