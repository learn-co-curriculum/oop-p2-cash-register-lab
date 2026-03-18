# Cash Register OOP Project

## Overview

This project implements a simple **Cash Register system** using Object-Oriented Programming in Python. It supports adding items, tracking totals, applying discounts, and managing transactions.

---

## Core Logic

### Initialization

* The `CashRegister` class is initialized with:

  * `discount` (optional, default = 0)
  * `total` → starts at `0`
  * `items` → empty list
  * `previous_transactions` → empty list

* Discount is validated:

  * Must be an integer
  * Must be between `0–100`
  * Invalid values default to `0`

---

### Adding Items

Method: `add_item(item, price, quantity=1)`

* Updates total:

  * `total += price × quantity`
* Adds item(s) to `items` list:

  * Includes duplicates based on quantity
* Stores transaction:

  ```python
  {
    "item": item,
    "price": price,
    "quantity": quantity
  }
  ```

---

### Applying Discount

Method: `apply_discount()`

* If discount is `0`:

  * Prints: `"There is no discount to apply."`
* Otherwise:

  * Applies percentage reduction:

    * `total = total × (1 - discount/100)`
  * Prints updated total in format:

    * `"After the discount, the total comes to $X."`

---

### Voiding Last Transaction

Method: `void_last_transaction()`

* Removes last transaction from history
* Deducts its value from total
* Removes corresponding items from `items` list
* Ensures total does not go below `0`

---

## Key Behaviors

* Supports multiple quantities per item
* Maintains transaction history
* Handles edge cases (empty transactions, invalid discounts)
* Ensures accurate total updates at all times

---

