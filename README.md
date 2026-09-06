# Cash Register OOP Lab

## About

This project is a Python Object-Oriented Programming (OOP) exercise that models a simple cash register for an e-commerce store.

The `CashRegister` class can:

* Add items to the register
* Calculate the total price
* Handle different quantities
* Apply percentage discounts
* Keep track of previous transactions
* Void the most recent transaction
* Validate discount values

## Features

### Add Items

Items can be added with a price and an optional quantity.

```python
register.add_item("eggs", 0.98)
register.add_item("book", 5.00, 3)
```

The quantity is used to calculate the total and to store the correct number of items.

### Discounts

The cash register accepts a discount between `0` and `100` percent.

```python
register = CashRegister(20)
```

A 20% discount reduces the total by 20%.

Invalid discounts are rejected with:

```text
Not valid discount
```

If there is no discount to apply, the program displays:

```text
There is no discount to apply.
```

### Void Last Transaction

The register keeps a record of previous transactions. The latest transaction can be removed using:

```python
register.void_last_transaction()
```

This updates both the total and the items list.

## Technologies

* Python 3
* Object-Oriented Programming
* Pytest
* Git
* GitHub

## Project Structure

```text
oop-p2-cash-register-lab/
│
├── cash_register.py
├── README.md
├── pytest.ini
└── lib/
    └── testing/
        └── cash_register_test.py
```

## Testing

The project uses `pytest` to test the CashRegister class.

Run the tests with:

```bash
pytest
```

The tests check:

* CashRegister initialization
* Discount handling
* Total calculation
* Adding items
* Adding multiple quantities
* Applying discounts
* Empty discount handling
* Tracking items
* Voiding transactions

## Screenshot

The completed project and passing tests are shown below.

![Cash Register Tests](screenshots/cash-register-tests.png)

## Git Workflow

This project was developed using a feature branch workflow.

The feature branch was created from `main`, changes were committed and pushed to GitHub, and a pull request was opened and merged into `main`.

## Author

JeYBee
