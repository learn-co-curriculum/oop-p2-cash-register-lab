#!/usr/bin/env python3

class CashRegister:
  def __init__(self,discount:(int)=0):
    self.total=0
    self.items=[]
    self.previous_transactions=[]
    if discount<0 or discount>100:
      print("Not valid discount")
      self.discount=0
    else:
      self.discount=discount
  def add_item(self, item, price, quantity=1): 
    self.total += price * quantity
    for _ in range(quantity): 
      self.items.append(item) 
      self.previous_transactions.append((item, price, quantity))
  def apply_discount(self):
    if self.discount == 0:
        print("There is no discount to apply.")
        return

    self.total -= self.total * (self.discount / 100)
    print(f"After the discount, the total comes to ${self.total:.0f}.")
  def void_last_transaction(self): 
    if len(self.previous_transactions) == 0: 
      return 
    item, price, quantity = self.previous_transactions.pop() 
    self.total -= price * quantity 
    for _ in range(quantity): 
      self.items.remove(item)