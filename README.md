# Cash Register Lab - Object Oriented Programming (OOP)

## Overview
This lab implements a **Cash Register** using Python classes and object-oriented programming principles.  
The Cash Register allows you to:

- Add items with prices and quantities  
- Apply a discount to the total  
- Void the last transaction  
- Track items and previous transactions  

---

## Features / Attributes

| Attribute | Description |
|-----------|-------------|
| `discount` | Percentage discount (0-100) |
| `total` | Current total price of all items |
| `items` | List of items in the register |
| `previous_transactions` | List of past transactions for voiding |

---

## Methods

| Method | Description |
|--------|------------|
| `add_item(item, price, quantity=1)` | Adds an item to the register and updates total |
| `apply_discount()` | Applies the discount to total, removes last transaction if any |
| `void_last_transaction()` | Removes the last transaction and updates total/items |

---

## Usage Example

```python
from cash_register import CashRegister

# Create a register with 20% discount
register = CashRegister(20)

# Add items
register.add_item("MacBook Air", 1000)
register.add_item("Mouse", 50)

print(register.total)   # 1050
print(register.items)   # ['MacBook Air', 'Mouse']

# Apply discount
register.apply_discount()  
# Prints: After the discount, the total comes to $840.

# Void last transaction
register.void_last_transaction()
# Prints: Voided last transaction: Mouse
