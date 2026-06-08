#!/usr/bin/env python3

class CashRegister:
  #Initialize the instances
  def __init__ (self, discount=0):
    self.discount = discount
    self.total = 0.0
    self.items = []
    self.previous_transactions = []
  
  #decorator for discount
  @property
  def discount (self):
    return self._discount
  
  @discount.setter
  def discount (self, discount_input):
    if isinstance(discount_input, int) and 0 <= discount_input <= 100:
        self._discount = discount_input
    else:
         raise ValueError("Not valid discount")
  
  #method to add items
  def add_item(self, item, price, quantity):
      self.total += price * quantity
      self.items.append(item)
      transaction_record ={
         "item": item,
         "price": price,
         "quantity": quantity
      }
      self.previous_transactions.append(transaction_record)

# Method to apply_discount
  def apply_discount (self):
      if len(self.previous_transactions) == 0:
         print("There is no discount to apply.")
         return
#  Apply discount as percentage off from total
      total_discount = self.total * (self.discount/100)
      self.total -= total_discount
      
#  Remove the last item of previous_transaction from array
      last_transaction = self.previous_transactions.pop()

#  Ensure items reflects correctly (remove the item from self.items)
      if last_transaction["item"] in self.item:
         self.items.remove(last_transaction["item"])
 
#  Ensure price reflects correctly      
   #Since we just discounted the total, but removed an item, we adjust the total 
   #by subtracting the discounted value of that removed item.
      item_cost = last_transaction["price"] * last_transaction["quantity"]
      discounted_item_cost = item_cost * (1 - (self.discount / 100))
      self.total -= discounted_item_cost
      return self.total
  
  
  #method to void_last_transaction
  def void_last_transaction(self):
    # Check if there's anything to void
        if not self.previous_transactions:
            print("No transactions to void.")
            return
        # Remove the last transaction
        last_transaction = self.previous_transactions.pop()
        # Remove from items list
        if last_transaction["item"] in self.items:
            self.items.remove(last_transaction["item"])
        # Subtract the cost of the voided item from the total
        item_cost = last_transaction["price"] * last_transaction["quantity"]
        self.total -= item_cost

        print(f"Voided: {last_transaction['item']}")

        
    






    
