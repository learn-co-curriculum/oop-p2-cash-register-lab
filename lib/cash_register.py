#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    # initialize CashRegister object.
    self._discount = discount
    # discont: percentage of total.
    self._total = 0
    # total: running total of all items.
    self._items = []
    #list of item names.
    self._previous_transactions = []
    # list of dicts recording each transaction
  
  @property  
  def discount(self):
    # returns the current discount percentage.
    return self._discount
  
  @discount.setter
  def discount(self, value):
    # Validating and setting discount.
    if isinstance(value, int) and 0 <= value <= 100:
      self._discount = value
    else:
      print("Not valid discount")
    # must be an integer btwn 0 - 100 .
    #if invalid, print an error message.  
  
  @property    
  def total(self):
    # return current total price of all items.
    return self._total
  
  @total.setter
  def total(self, value):
    self._total = value
  
  @property
  def items(self):
    # returns a list of items currently in the register
    return self._items
  
  @property
  def previous_transactions(self):
    #returns a list of previous transactions each as a dict
    return self._previous_transactions
    
  def add_item(self, item, price, quantity = 1):
    # add item to the register
    self._total += price * quantity
    # increase total by price * quantity
    for _ in range(quantity):
      self._items.append(item)
      self._previous_transactions.append({
        "item": item,
        "price": price,
        "quantity": quantity
    })
      #add item's' to items list
      # record transaction in previous_transactions
    
  def apply_discount(self):
    # applying discount to total
    if self._discount > 0:
      # if discount > 0 reduces total by percentage
      self._total = self._total - (self._total * (self._discount / 100))
      print(f"After the discount, the total comes to ${int(self._total)}.")
    else:
      print("There is no discount to apply.")
      #print message
      
  def void_last_transaction(self):
    # removes the last transaction from previous_transactions
    if self._previous_transactions:
      last_transaction  = self._previous_transactions.pop()
      self._total -= last_transaction["price"] * last_transaction["quantity"]
      for _ in range(last_transaction["quantity"]):
        if last_transaction["item"] in self._items:
          self._items.remove(last_transaction["item"])
      print("Last transaction voided")
    else:
      print("No transaction to void")                
      # adjusting the total by subtracting price * quantity
      # remove item's' from item list
      # print message 