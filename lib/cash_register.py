#!/usr/bin/env python3

  class CashRegister:

    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        
   