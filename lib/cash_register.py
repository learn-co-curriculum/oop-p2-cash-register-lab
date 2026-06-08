#!/usr/bin/env python3
#creating cash register class
class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total=0
    self.items = []
    self.previous_transaction = []

#property discount
  @property
  def discount(self):
    return self._discount

  @discount.setter
  def discount(self, value):
    if isinstance(value, int) and 0 <= value <= 100:
      self._discount = value
    else:
      print("Not valid discount")
      self._discount = 0

#method1 add_item      
def add_item(self, item, price, quantity=1):
    self.total += price * quantity
    self.items.append(item)
    self.previous_transaction.append({
      "item": item,
      "price": price,
      "quantity": quantity
    })
#method2 apply_discount
def apply_discount(self):
    if len(self.previous_transaction) == 0:
      print("There is no discount to apply.")
    else:
      last=self.previous_transaction.pop()
      self.total -= last["price"] * last["quantity"]
      self.items.remove(last["item"])

#method3 void_last_transaction
def void_last_transaction(self):
    if len(self.previous_transaction) == 0:
      print(" No transaction to void.")
    else:
        last=self.previous_transaction.pop()
        self.total -= last["price"] * last["quantity"]
        self.items.remove(last["item"])           
  pass
