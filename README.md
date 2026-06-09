# Cash Register Lab

A simple Python cash register app. It can add items, keep track of the total, apply a discount, and void the last transaction.

## Features

- Create a cash register.
- Add items and quantities.
- Track the total price.
- Apply a discount.
- Void the last transaction.
- Keep a list of added items.

## Project Structure

```text
.
├── lib
│   ├── cash_register.py
│   └── testing
│       └── cash_register_test.py
└── README.md
```

## Tools & Resources

- [GitHub Repo](https://github.com/learn-co-curriculum/oop-p2-cash-register-lab)
- [Python Classes](https://docs.python.org/3/tutorial/classes.html)

## Getting Started

Install `pytest` if needed:

```bash
pip install pytest
```

Run the test suite from the project root:

```bash
pytest lib/testing/cash_register_test.py
```

## Usage

Example:

```python
from cash_register import CashRegister

register = CashRegister(20)

register.add_item("macbook air", 1000)
register.apply_discount()

print(register.total)
print(register.items)
```

Output:

```text
After the discount, the total comes to $800.
800.0
['macbook air']
```

## CashRegister Behavior

### Creating a Register

```python
register = CashRegister()
discounted_register = CashRegister(20)
```

If no discount is given, the discount starts at `0`. The total starts at `0`, and the items list starts empty.

### Adding Items

```python
register.add_item("eggs", 1.99)
register.add_item("tomato", 1.76, 3)
```

`add_item()` adds the item to the register and increases the total.

### Applying a Discount

```python
register = CashRegister(20)
register.add_item("book", 10.00)
register.apply_discount()
```

`apply_discount()` takes the discount off the total. If there is no discount, it prints:

```text
There is no discount to apply.
```

### Voiding the Last Transaction

```python
register.add_item("apple", 0.99)
register.add_item("tomato", 1.76)
register.void_last_transaction()
```

`void_last_transaction()` removes the last item transaction and updates the total.

## Lab Instructions

### Task 1: Define the Problem

Build a model for a cash register that can:

- Build a cash register object.
- Add items.
- Apply discounts.
- Void previous transactions.

### Task 2: Determine the Design

The `CashRegister` class should include these attributes:

- `discount`
- `total`
- `items`
- `previous_transactions`

The `CashRegister` class should include these methods:

- `add_item(item, price, quantity)`
- `apply_discount()`
- `void_last_transaction()`

### Task 3: Develop, Test, and Refine the Code

#### Step 1: Git Feature Branch

Create a feature branch for your work using git.

#### Step 2: Create a CashRegister Class

The `__init__` method should:

- Accept an optional discount argument.
- Initialize the discount to `0` if no discount is provided.
- Treat the discount as a percentage off the total price.
- Initialize `total` to `0`.
- Initialize `items` as an empty list.
- Initialize `previous_transactions` as an empty list.

#### Step 3: Properties

The `discount` property should:

- Ensure the discount is an integer.
- Ensure the discount is between `0` and `100`, inclusive.
- Print `Not valid discount` if the value is invalid.

#### Step 4: Methods

`add_item(item, price, quantity)` should:

- Add the item's price to the total.
- Add the item to the items list.
- Add a transaction with the item, price, and quantity.

`apply_discount()` should:

- Apply the register's discount percentage to the total.
- Print `There is no discount to apply.` if there is no discount.

`void_last_transaction()` should:

- Remove the most recent transaction.
- Update the total correctly.
- Update the items list correctly.
- Print `There is no transaction to void.` if there are no transactions.

#### Step 5: Push Feature Branch and Open a PR on GitHub

- Save, commit, and push your code to GitHub.
- Open a PR on the main branch of your own repo.
- Do not open a PR on the original `learn-co-curriculum` repo.

#### Step 6: Merge to Main

Review the PR and merge your finished code into the main branch.

## Tests

The tests check that the register:

- Starts with the correct values.
- Adds items correctly.
- Applies discounts.
- Tracks items.
- Voids the last transaction.

## Document and Maintain

Best practice documentation steps:

- Add comments to code to explain purpose and logic.
- Clarify intent and functionality for other developers.
- Add a screenshot of completed work in the README if needed.
- Update README text to reflect the functionality of the application.
- Delete any stale branches on GitHub.
- Remove unnecessary or commented-out code.
- Update `.gitignore` if needed to avoid committing sensitive data.

## Save Your Work and Push to GitHub

Before submitting your solution:

1. Add your changes to the staging area:

```bash
git add .
```

2. Create a commit:

```bash
git commit -m "Update README documentation"
```

3. Push your commits to GitHub:

```bash
git push origin main
```

Use `git branch` to check whether your branch is named `main` or `master`.

## Submission and Grading Criteria

1. Use the rubric in Canvas as a guide for how this lab is graded.
2. Your submission will be automatically scored in CodeGrade using the most recent commit.
3. Make sure you have pushed your commit to GitHub before submitting your assignment.
4. Review your submission in CodeGrade and check your final score in your Canvas gradebook.
5. When you are ready to submit, click the **Load Lab: Object Oriented Programming (OOP)- Part 2- Cash Register** button in Canvas to launch CodeGrade.
6. Click **+ Create Submission** and connect your repository for this lab.

For additional information on submitting assignments in CodeGrade, review [Getting Started in Canvas](https://help.codegrade.com/for-students/getting-started/getting-started-in-canvas).

## Screenshot of passing test

![Screenshot](Assets/Screenshot.png)
