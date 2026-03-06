# CashRegister class - Simulates cash register for e-commerce

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []
    
    def add_item(self, item, price, quantity=1):
        # Add price * quantity to total
        self.total += price * quantity
        
        # Add item to items array (once per quantity)
        for i in range(quantity):
            self.items.append(item)
        
        # Add transaction to previous_transactions
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })
    
    def apply_discount(self):
        # Apply discount percentage to total
        if self.discount > 0:
            self.total = self.total - (self.total * self.discount / 100)
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")
    
    def void_last_transaction(self):
        # Remove last transaction and adjust total/items
        if self.previous_transactions:
            last_transaction = self.previous_transactions.pop()
            
            # Subtract from total
            self.total -= last_transaction["price"] * last_transaction["quantity"]
            
            # Remove items from items list
            for i in range(last_transaction["quantity"]):
                self.items.remove(last_transaction["item"])
        else:
            print("There is no transaction to void.")