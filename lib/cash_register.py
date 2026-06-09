#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self._discount = discount
    self._total = 0
    self._items = []
    self._previous_transaction = []
  
  @property  
  def discount(self):
    return self._discount
  
  @discount.setter
  def discount(self, value):
    if isinstance(value, int) and 0 <= value <= 100:
      self._discount = value
    else:
      print("Not valid discount")
  
  @property    
  def total(self):
    return self._total
  
  @total.setter
  def total(self, value):
    self._total = value
  
  @property
  def items(self):
    return self._items
  
  @property
  def previous_transaction(self):
    return self._previous_transaction
    
  def add_item(self, item, price, quantity = 1):
    self._total += price * quantity
    for _ in range(quantity):
      self._items.append(item)
      self._previous_transaction.append({
        "item": item,
        "price": price,
        "quantity": quantity
    })
    
  def apply_discount(self):
    if self._discount > 0:
      self._total = self._total - (self._total * (self._discount / 100))
      print(f"After the discount, the total comes to ${int(self._total)}.")
    else:
      print("There is no discount to apply.")
      
  def void_last_transaction(self):
    if self._previous_transaction:
      last_transaction  = self._previous_transaction.pop()
      self._total -= last_transaction["price"] * last_transaction["quantity"]
      for _ in range(last_transaction["quantity"]):
        if last_transaction["item"] in self._items:
          self._items.remove(last_transaction["item"])
      print("Last transaction voided")
    else:
      print("No transaction to void")                 