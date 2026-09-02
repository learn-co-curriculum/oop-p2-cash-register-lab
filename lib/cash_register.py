#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0, total=0, items=None, previous_transactions=None):
    # Keep the register ready for use even when an invalid discount is supplied.
    self._discount = 0
    self.discount = discount
    self.total = total
    self.items = items if items is not None else []
    self.previous_transactions = previous_transactions if previous_transactions is not None else []

  @property
  def discount(self):
    return self._discount

  @discount.setter
  def discount(self, value):
    # Discounts represent percentages and must stay within the valid range.
    if isinstance(value, int) and not isinstance(value, bool) and 0 <= value <= 100:
      self._discount = value
    else:
      print("Not valid discount")

  def add_item(self, item, price, quantity=1):
    # Store one transaction while expanding items for the register's item list.
    self.total += price * quantity
    self.items.extend([item] * quantity)
    self.previous_transactions.append({
      "item": item,
      "price": price,
      "quantity": quantity
    })

  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
      return

    self.total -= self.total * self.discount / 100
    print(f"After the discount, the total comes to ${self.total:g}.")

  def void_last_transaction(self):
    if not self.previous_transactions:
      return

    # Reverse the most recent transaction and remove its expanded item entries.
    transaction = self.previous_transactions.pop()
    self.total -= transaction["price"] * transaction["quantity"]
    del self.items[-transaction["quantity"]:]
