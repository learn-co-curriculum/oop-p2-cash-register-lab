# Object Oriented Programming (OOP) Part 2 - Cash Register Lab

A Python implementation of a cash register that supports adding items, applying percentage discounts, and voiding the last transaction.

## Features

- Add items with optional quantity
- Apply a percentage discount to the running total
- Void the most recent transaction
- Validates discount values (must be an integer between 0–100)

## Usage

```python
from cash_register import CashRegister

# Create a register with a 20% discount
register = CashRegister(20)

register.add_item("apples", 1.50, 3)   # adds 3 apples at $1.50 each
register.add_item("bread", 2.99)        # adds 1 loaf of bread

print(register.total)          # 7.49
print(register.items)          # ['apples', 'apples', 'apples', 'bread']

register.apply_discount()      # After the discount, the total comes to $5.
register.void_last_transaction()  # removes last add_item call
```

## Class Reference

### `CashRegister(discount=0)`

| Attribute               | Type  | Description                                    |
|-------------------------|-------|------------------------------------------------|
| `discount`              | int   | Percentage off (0–100). Validated via property.|
| `total`                 | float | Running price total.                           |
| `items`                 | list  | Flat list of item names (expanded by quantity).|
| `previous_transactions` | list  | List of `{item, price, quantity}` dicts.       |

| Method                         | Description                                                             |
|--------------------------------|-------------------------------------------------------------------------|
| `add_item(item, price, qty=1)` | Adds an item, updates total and transaction history.                    |
| `apply_discount()`             | Deducts `discount`% from total; prints result. Requires `discount > 0`.|
| `void_last_transaction()`      | Reverses the most recent `add_item` call.                               |

## Screenshot

![All 14 tests passing](https://i.imgur.com/placeholder.png)

> Run tests with: `python3 -m pytest lib/testing/cash_register_test.py -v`

## Tools & Resources

- [Python Classes](https://docs.python.org/3/tutorial/classes.html)
- [pytest](https://docs.pytest.org/)
