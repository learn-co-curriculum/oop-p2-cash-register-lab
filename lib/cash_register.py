#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.previous_transactions = []
  @property
  def discount(self):
    return self._discount

  @discount.setter
  def discount(self, value):
    if isinstance(value, int) and 0 <= value <= 100:
      self._discount = value
    else:
      print("Not valid discount")

  def add_item(self, item, price, quantity):
    self.total += price * quantity
    self.items.append(item)

    transaction ={
      "item": item,
      "price": price,
      "quantity": quantity
    }
    self.previous_transactions.append(transaction)

  def apply_discount(self):
    if not self.previous_transactions:
      print("There is no discount to apply.")
      return

    self.total -= self.total * (self.discount / 100)
    last_transaction = self.previous_transactions.pop()
    self.items.pop()

  def void_last_transaction(self):
    if not self.previous_transactions:
      return

    last_transaction = self.previous_transactions.pop()
    cost = last_transaction["price"] * last_transaction["quantity"]
    self.total -= cost
    self.items.pop()

 
