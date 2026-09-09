#!/usr/bin/env python3


# The CashRegister class represents a simple cash register.
#
# Each CashRegister object keeps track of:
#   1. The discount available to the customer.
#   2. The current total cost.
#   3. All items that have been added.
#   4. Previous transactions so that the latest transaction
#      can be reversed if necessary.
#
# This class demonstrates important Object-Oriented Programming
# concepts including:
#
#   - Classes and objects
#   - Constructors (__init__)
#   - Instance attributes
#   - Instance methods
#   - Properties
#   - Property setters
#   - Decorators (@property)
#   - Encapsulation
#
class CashRegister:

    # __init__ is the constructor.
    #
    # It runs automatically whenever a new CashRegister object
    # is created.
    #
    # discount=0 means that if the user does not supply a discount,
    # the register starts with no discount.
    #
    # Example:
    #   CashRegister()    -> discount is 0
    #   CashRegister(20)  -> discount is 20
    #
    def __init__(self, discount=0):

        # Assigning through self.discount calls our property setter.
        # This allows the discount value to be validated.
        self.discount = discount

        # The register begins with a total of zero because no items
        # have been purchased yet.
        self.total = 0

        # This list stores the names of all items added to the register.
        self.items = []

        # This list stores details about each add_item() operation.
        # It allows us to reverse the most recent transaction later.
        self.previous_transactions = []

    # @property allows us to access _discount using:
    #
    #   register.discount
    #
    # rather than accessing _discount directly.
    #
    @property
    def discount(self):
        return self._discount

    # The setter controls what values are allowed to be assigned
    # to discount.
    #
    # A valid discount must:
    #   - be an integer
    #   - be between 0 and 100 inclusive
    #
    @discount.setter
    def discount(self, value):

        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value

        else:
            print("Not valid discount")
            self._discount = 0

    # add_item() adds a product to the cash register.
    #
    # Parameters:
    #   item     -> product name
    #   price    -> price of one item
    #   quantity -> number being purchased
    #
    # quantity defaults to 1 so this is valid:
    #
    #   add_item("eggs", 1.99)
    #
    # and so is:
    #
    #   add_item("eggs", 1.99, 3)
    #
    def add_item(self, item, price, quantity=1):

        # Work out the total cost of this particular transaction.
        transaction_total = price * quantity

        # Add the transaction amount to the existing register total.
        self.total += transaction_total

        # Add the item to the items list once for every unit purchased.
        #
        # For example:
        #
        #   add_item("egg", 1, 3)
        #
        # produces:
        #
        #   ["egg", "egg", "egg"]
        #
        for _ in range(quantity):
            self.items.append(item)

        # Store enough information to undo this transaction later.
        transaction = {
            "item": item,
            "price": price,
            "quantity": quantity
        }

        self.previous_transactions.append(transaction)

    # apply_discount() reduces the current total using the
    # register's discount percentage.
    #
    # For example:
    #
    #   total = 1000
    #   discount = 20
    #
    #   discount amount = 1000 * 20 / 100
    #                   = 200
    #
    #   final total = 1000 - 200
    #               = 800
    #
    def apply_discount(self):

        # A zero discount means there is nothing to apply.
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        # Calculate how much money should be removed from the total.
        discount_amount = self.total * (self.discount / 100)

        # Reduce the current total.
        self.total -= discount_amount

        # :g avoids unnecessary trailing ".0".
        #
        # Example:
        #   800.0 -> 800
        #   72.5  -> 72.5
        #
        print(
            f"After the discount, the total comes to ${self.total:g}."
        )

    # void_last_transaction() reverses the most recent add_item()
    # transaction.
    #
    # It must:
    #   1. Find the most recent transaction.
    #   2. Remove its cost from total.
    #   3. Remove its items from the items list.
    #   4. Remove it from previous_transactions.
    #
    def void_last_transaction(self):

        # If there are no previous transactions, there is
        # nothing that can be reversed.
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        # pop() removes and returns the final transaction.
        last_transaction = self.previous_transactions.pop()

        # Extract information from the transaction dictionary.
        price = last_transaction["price"]
        quantity = last_transaction["quantity"]

        # Calculate the full amount that transaction contributed.
        transaction_total = price * quantity

        # Remove the transaction amount from the register total.
        self.total -= transaction_total

        # Remove each item belonging to that transaction.
        for _ in range(quantity):
            self.items.pop()