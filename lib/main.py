from cash_register import CashRegister

def main():
   
    register = CashRegister()

    
    register.add_item("Book", 20, 2)
    register.add_item("Coffee", 5, 1)
    register.apply_discount()
    register.void_last_transaction()

if __name__ == "__main__":
    main()