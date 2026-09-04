class CashRegister {
  constructor(discount = 0) {
    this.discount = discount;
    this.total = 0;
    this.items = [];
    this.previous_transactions = [];
  }

  get discount() {
    return this._discount;
  }

  set discount(value) {
    if (Number.isInteger(value) && value >= 0 && value <= 100) {
      this._discount = value;
    } else {
      console.log("Not valid discount");
      this._discount = 0;
    }
  }

  add_item(item, price, quantity) {
    this.total += price * quantity;

    this.items.push({
      item: item,
      price: price,
      quantity: quantity
    });

    this.previous_transactions.push({
      item: item,
      price: price,
      quantity: quantity
    });
  }

  apply_discount() {
    if (this.previous_transactions.length === 0) {
      console.log("There is no discount to apply.");
      return;
    }

    this.total = this.total * ((100 - this.discount) / 100);
  }

  void_last_transaction() {
    if (this.previous_transactions.length === 0) {
      return;
    }

    const transaction = this.previous_transactions.pop();

    this.total -= transaction.price * transaction.quantity;

    this.items.pop();
  }
}
