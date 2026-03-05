class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount
    
    @discount.setter
    def discount(self, value):
        if type(value) != int or value < 0 or value > 100:
            print("Not valid discount")
        else:
            self._discount = value

    def add_item(self, item, price, quantity=1):
        
        self.total += price * quantity
        
        self.items.append(item)

        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):

        if not self.previous_transactions:
            print("There is no discount to apply.")
            return
        
        last = self.previous_transactions.pop()
        self.total -= last["price"] * last["quantity"]
        
        if last["item"] in self.items:
            self.items.remove(last["item"])
        
        
        self.total = self.total * ((100 - self.discount) / 100)

    def void_last_transaction(self):
      
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return
        

        last = self.previous_transactions.pop()
        self.total -= last["price"] * last["quantity"]
        

        if last["item"] in self.items:
            self.items.remove(last["item"])
