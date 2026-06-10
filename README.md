# Cash Register Application

## Overview

This project implements a **Cash Register** system in Python that simulates the core functionality of a cash register for an e-commerce platform. The application allows users to add items to a cart, apply discounts, track transactions, and void the most recent transaction.

## Features

* Add items to the cash register.
* Calculate and update the running total.
* Store purchased items.
* Track previous transactions.
* Apply percentage-based discounts.
* Void the most recent transaction.
* Validate discount values to ensure they are between 0 and 100.

## Class: CashRegister

### Attributes

| Attribute               | Description                                                                     |
| ----------------------- | ------------------------------------------------------------------------------- |
| `discount`              | Percentage discount applied to the total. Must be an integer between 0 and 100. |
| `total`                 | Running total cost of all items in the register.                                |
| `items`                 | List containing all items added to the register.                                |
| `previous_transactions` | List of transaction records containing item, price, and quantity information.   |

### Methods

#### `add_item(item, price, quantity)`

Adds an item to the cash register.

**Parameters:**

* `item` (str): Name of the item.
* `price` (float/int): Price of a single item.
* `quantity` (int): Number of items purchased.

**Functionality:**

* Updates the total price.
* Adds the item(s) to the items list.
* Records the transaction in `previous_transactions`.

---

#### `apply_discount()`

Applies the configured discount percentage to the current total.

**Functionality:**

* Calculates the discount amount.
* Reduces the total by the discount percentage.
* Displays a message if there are no transactions available.

---

#### `void_last_transaction()`

Removes the most recent transaction from the register.

**Functionality:**

* Removes the last transaction from `previous_transactions`.
* Deducts the transaction amount from the total.
* Removes the corresponding item(s) from the items list.
* Displays a message if there are no transactions to void.

## Installation

1. Clone the repository:

```bash
git clone git@github.com:wanja-juma/oop-p2-cash-register-lab.git
```

2. Navigate to the project directory:

```bash
cd cash-register
```

3. Run the application:

```bash
python cash_register.py
```

## Example Usage

```python
register = CashRegister(20)

register.add_item("Laptop", 1000, 1)
register.add_item("Mouse", 50, 2)

print(register.total)
# 1100

register.apply_discount()
print(register.total)
# 880.0

register.void_last_transaction()
print(register.total)

print(register.items)
```

## Validation Rules

* Discount must be an integer.
* Discount must be between 0 and 100 inclusive.
* Invalid discounts display the message:

```text
Not valid discount
```

### screen Disply

Screenshot 2026-06-10 162458.png

## Future Improvements

* Support multiple discount codes.
* Generate receipts.
* Save transaction history to a file or database.
* Add tax calculation.
* Support item removal by name.

## Author

Developed as part of an Object-Oriented Programming exercise to demonstrate class design, state management, and transaction handling in Python.

