#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self._discount = discount
    self.total = 0
    self.items = []
    self.previous_transactions = []
  
  @property
  def discount(self):
    return self._discount
  
  @discount.setter
  def discount (self, value):
    if isinstance(value, int) and  0 <= value <= 100:
      self._discount = value
    else:
      print("Not valid discount")
  
  def add_item(self, item, price, quantity= 1):
    self.total += price * quantity

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

    if not self.previous_transactions:
        print("There is no discount to apply.")
        return

    # Apply discount
    discount_amount = self.total * (self.discount / 100)
    self.total -= discount_amount
    print(f"After the discount, the total comes to ${int(self.total)}.")


    # Remove last transaction
    last_action = self.previous_transactions.pop()

    # Remove items from the items list
    for _ in range(last_action["quantity"]):
        self.items.remove(last_action["item"])



  def void_last_transaction(self):
    if not self.previous_transactions:
        print("There is no transaction to void.")
        return

    last_action = self.previous_transactions.pop()

    item_name = last_action["item"]
    item_price = last_action["price"]
    item_qty = last_action["quantity"]

    self.total -= item_price * item_qty

    for _ in range(item_qty):
        self.items.remove(item_name)

    
  
