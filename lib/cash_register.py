class CashRegister:
    """
    CashRegister class simulates a simple cash register for an e-commerce site.

    Attributes:
        discount (int): Discount percentage for the total (0-100)
        total (float): Current total amount
        items (list): List of items added
        previous_transactions (list): History of previous transactions
    """

    def __init__(self, discount=0):
        """
        Initialize a CashRegister instance.
        discount: optional, default is 0
        """
        if isinstance(discount, int) and 0 <= discount <= 100:
            self._discount = discount
        else:
            print("Not valid discount")
            self._discount = 0

        self.total = 0
        self.items = []
        self.previous_transactions = []

    # Discount property with validation
    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        """
        Add item(s) to the register.
        Updates total, items list, and previous transactions.
        """
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(item)
        self.previous_transactions.append({'item': item, 'price': price, 'quantity': quantity})

    def apply_discount(self):
        """
        Apply the discount to the current total.
        Prints the updated total.
        """
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return

        discount_amount = self.total * (self._discount / 100)
        self.total -= discount_amount
        print(f"After applying discount of {self._discount}%, the total is: ${self.total:.2f}")

    def void_last_transaction(self):
        """
        Remove the last transaction and update total and items.
        """
        if not self.previous_transactions:
            print("No transaction to void.")
            return

        last_transaction = self.previous_transactions.pop()
        self.total -= last_transaction['price'] * last_transaction['quantity']
        for _ in range(last_transaction['quantity']):
            self.items.pop()