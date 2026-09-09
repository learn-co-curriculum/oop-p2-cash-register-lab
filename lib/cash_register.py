class CashRegister:
    """
    A Cash Register class that simulates an e-commerce checkout system.
    
    This class handles adding items, applying discounts, and managing
    transaction history for a simple point-of-sale system.
    """
    
    def __init__(self, discount=0):
        """
        Initialize a new CashRegister instance.
        
        Args:
            discount (int, optional): Discount percentage to apply to total.
                                      Defaults to 0. Must be between 0-100.
        """
        # Initialize attributes
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []
    
    def add_item(self, item, price, quantity=1):
        """
        Add an item to the cash register.
        
        Args:
            item (str): Name of the item
            price (float): Price per unit of the item
            quantity (int, optional): Number of items to add. Defaults to 1.
        """
        # Add price to total (price * quantity)
        self.total += price * quantity
        
        # Add item to items array (repeat for each quantity)
        for _ in range(quantity):
            self.items.append(item)
        
        # Add transaction record
        transaction = {
            'item': item,
            'price': price,
            'quantity': quantity
        }
        self.previous_transactions.append(transaction)
    
    def apply_discount(self):
        """
        Apply discount to the total price.
        
        Calculates discounted total and updates the total attribute.
        
        Returns:
            str: Message indicating the discount applied or error
        """
        # Check if there is a discount to apply
        if self.discount == 0:
            print("There is no discount to apply.")
            return "There is no discount to apply."
        
        # Calculate discounted total
        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount
        
        # Print the success message
        print(f"After the discount, the total comes to ${int(self.total)}.")
        return f"After the discount, the total comes to ${int(self.total)}."
    
    def void_last_transaction(self):
        """
        Void/remove the most recent transaction.
        
        Removes the last transaction from previous_transactions,
        updates total, and removes corresponding items from items list.
        """
        # Check if there are transactions to void
        if not self.previous_transactions:
            print("No transactions to void.")
            return
        
        # Get the last transaction
        last_transaction = self.previous_transactions.pop()
        
        # Subtract the price from total
        self.total -= last_transaction['price'] * last_transaction['quantity']
        
        # Remove items from items list
        for _ in range(last_transaction['quantity']):
            if self.items:
                self.items.pop()
    
    def get_total(self):
        """
        Get the current total.
        
        Returns:
            float: The current total price
        """
        return self.total
    
    def get_items(self):
        """
        Get the list of items.
        
        Returns:
            list: List of all item names
        """
        return self.items
    
    def get_previous_transactions(self):
        """
        Get the transaction history.
        
        Returns:
            list: List of all previous transactions
        """
        return self.previous_transactions
    
    def __str__(self):
        """
        String representation of the cash register.
        
        Returns:
            str: Human-readable summary of the cash register state
        """
        return f"CashRegister(total=${self.total:.2f}, items={len(self.items)}, transactions={len(self.previous_transactions)})"


# Example usage and testing
if __name__ == "__main__":
    # Create a cash register with 10% discount
    register = CashRegister(10)
    print(f"Created register with {register.discount}% discount")
    
    # Add some items
    register.add_item("Apple", 1.50, 3)
    register.add_item("Banana", 0.75, 2)
    register.add_item("Orange", 1.00, 1)
    
    print(f"Total before discount: ${register.get_total():.2f}")
    print(f"Items: {register.get_items()}")
    print(f"Transactions: {register.get_previous_transactions()}")
    
    # Apply discount
    register.apply_discount()
    print(f"Items after discount: {register.get_items()}")
    
    # Void the last transaction
    register.void_last_transaction()
    print(f"Total after voiding last transaction: ${register.get_total():.2f}")
    print(f"Items after voiding: {register.get_items()}")