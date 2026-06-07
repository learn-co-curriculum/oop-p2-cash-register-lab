# Cash Register

A simple Python-based cash register model that supports adding items, applying discounts, and voiding transactions.

## Features

- **Initialization**: Create a `CashRegister` object with an optional discount percentage.
- **Add Items**: Add items by name, price, and quantity.
- **Apply Discounts**: Apply a percentage-based discount to the total.
- **Void Transactions**: Undo the last transaction, updating the total and item list automatically.

## Usage

```python
from lib.cash_register import CashRegister

# Create a register with a 20% discount
register = CashRegister(20)

# Add items
register.add_item("eggs", 2.50, 2)
register.add_item("milk", 3.00)

print(register.total) # Output: 8.0

# Apply the 20% discount
register.apply_discount() # Output: After the discount, the total comes to $6.4.

# Void the last transaction (milk)
register.void_last_transaction()
```

## Implementation Details

The `CashRegister` class uses:
- `@property` for the `discount` attribute to ensure it remains an integer between 0 and 100.
- A list of `previous_transactions` to track and revert changes if a transaction is voided.
- Automatic updates to the `total` and `items` list.

## Screenshots

![Cash Register Output](screenshot.png)
*(Note: This is a placeholder for a screenshot of the application in action.)*

## Testing

Run the tests using `pytest`:

```bash
pytest lib/testing/cash_register_test.py
```
