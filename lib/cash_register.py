#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self._discount = 0
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

  def add_item(self, item, price, quantity=1):
    subtotal = price * quantity
    self.total = round(self.total + subtotal, 2)

    for _ in range(quantity):
      self.items.append(item)

    self.previous_transactions.append(
      {
        "item": item,
        "price": price,
        "quantity": quantity,
        "subtotal": subtotal,
      }
    )

  def apply_discount(self):
    if not self.previous_transactions:
      print("There is no discount to apply.")
      return

    discount_amount = self.total * (self.discount / 100)
    self.total = round(self.total - discount_amount, 2)
    print(f"After the discount, the total comes to ${self.total:.0f}.")

  def void_last_transaction(self):
    if not self.previous_transactions:
      print("There is no transaction to void.")
      return

    last_transaction = self.previous_transactions.pop()
    subtotal = last_transaction["subtotal"]
    quantity = last_transaction["quantity"]

    self.total = round(self.total - subtotal, 2)

    for _ in range(quantity):
      if self.items:
        self.items.pop()

    if self.total < 0:
      self.total = 0
