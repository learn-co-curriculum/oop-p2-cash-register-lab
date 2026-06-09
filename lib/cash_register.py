#!/usr/bin/env python3


  class CashRegister:
  def __init__(self,discount=0):
    self._discount = discount 
    self.total = 0
    self.items = []
    self.previous_transactions =[]


  @property
  def discount(self):
    return self._discount 
  
  @discount.setter
  def discount (self,value):
    if isinstance(value,int) and 0 < value <= 100:
      self._discount =value
    else:  
      print('Not valid discount')

  
    


  def add_item(self,item,price,quantity=1):
    self.total += price * quantity

    self.items.append(item)

    self.previous_transactions.append(price*quantity)



  def apply_discount(self):
    if self._discount > 0:
       self.total -= self.total * self._discount /100
       print(f'After the discount, the total comes to ${self.total:.2f}.')
    else:  
       print('There is no discount to apply.')

  def void_last_transaction(self):
    self.items.pop()
    self.total -= self.previous_transactions.pop()
       
