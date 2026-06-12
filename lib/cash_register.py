#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount):
    self.discount = discount
    self.total = 0
    self.items = []
    self._last_transaction = 0

  @property
  def discount(self):
    return self._discount
  
  @discount.setter
  def discount(self, value):
      if (0 <= value <= 1):
        self._discount = value
      else:
        ValueError("Discount must be between 0 and 1")
  
  def add_item(self, title, price, quantity=1):
    amount = price * quantity
    self.total += amount
    self.last_transaction = amount

    for _ in range(quantity):
      self.items.append(title)

  def apply_discount(self):
    if self.discount > 0:
      self.total -= self.total * (self.discount / 100)
      print(f"After the discount the total come to {int(self.total)}")
    else:
      print("No discount")

  def void_last_transaction(self):
    self.total -= self._last_transaction
    self.last_transaction = 0