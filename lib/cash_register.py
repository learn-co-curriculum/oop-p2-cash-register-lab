#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.previous_transactions = []
    
  @classmethod
  def from_input(cls):
    user_input = input("Enter discount percentage or press enter for 0: ").strip()
    discount = int(user_input) if user_input else 0
    return cls(discount)
  
  @property
  def discount(self):
    return self._discount

  @discount.setter
  def discount(self, value):
    if 0 <= value <= 100 and isinstance(value, int):
      self._discount = value
    else:
      print("Not valid discount")
      
  def add_item(self, item, price, quantity = 1):
    self.total += price * quantity
    for i in range(quantity):
      self.items.append(item)
    self.previous_transactions.append({"item": item, "price": price, "quantity": quantity})
    
  def apply_discount(self,):
    if self.discount == 0 :
      print("There is no discount to apply.")
    else:
      total_discount = (self.total * self.discount)/100
      self.total = self.total - total_discount
      print(f"After the discount, the total comes to ${int(self.total)}.")
    
  def void_last_transaction(self):
    if self.previous_transactions == []:
      print("There is no transaction to void")
    else:
      last_item = self.previous_transactions.pop() 
      self.total -= last_item["price"] * last_item["quantity"]
      self.items.remove(last_item["item"])

  
