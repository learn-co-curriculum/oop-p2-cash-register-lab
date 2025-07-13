#!/usr/bin/env python3

class CashRegister:
  def __init__ (self, discount=0):
    self._discount = discount
    self.total = 0
    self.items = []
    self.previous_transactions = []

  @property
  def discount(self):
    return self._discount 
  @discount.setter
  def discount(self, value):
    #checking that discount is an integer and a number from 0-100 (inclusive)
    if isinstance (value, int) and 0 <= value <= 100:
      self._discount = value
    else: print("Not valid discount") 
  
  def add_item(self, item, price, quantity=1):
    if quantity > 0:
      #adding item in items list as many times as the quality specifies
      for _ in range(quantity):
        self.items.append(item)
      #adding to total
      self.total += price*quantity
      #adding transaction on previous_transactions list
      self.previous_transactions.append({ "item" : item, 
                                      "price" : price,
                                      "quantity": quantity 
                                      })

  def apply_discount(self):
    if self._discount > 0:
      #subtracting discount percentage from total
      self.total -= self.total*self._discount/100
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    #if there are no previous transaction, set total to 0
    if len(self.previous_transactions) == 0:
      self.total = 0
    else: 
      # removing the last transaction's total from total
      self.total -= self.previous_transactions[-1]["price"]*self.previous_transactions[-1]["quantity"]

      #removing the last transaction's items from items list
      for _ in range(self.previous_transactions[-1]["quantity"]):
        self.items.pop()

      #removing the last transaction
      self.previous_transactions.pop()
      

