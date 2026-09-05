#!/usr/bin/env python3

class CashRegister:

    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.previous_transactions = []

      
        self._discount = 0
        self.discount = discount  

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        # Must be a whole number between 0 and 100 inclusive
        if isinstance(discount, int) and 0 <= discount <= 100:
            self._discount = discount
        else:
            print("Not valid discount")    
    
   
