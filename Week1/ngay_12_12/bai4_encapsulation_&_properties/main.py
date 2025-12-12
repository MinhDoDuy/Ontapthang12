from poly_magic import BankAccount, Temperature

def main():
    acc = BankAccount(1000)
    amount_deposit = float(input("Nhập số tiền cần nạp: "))
    acc.deposit(amount_deposit)
    amount_withdraw = float(input("Nhập số tiền cần rút: "))
    acc.withdraw(amount_withdraw)
    print("Current balance: ", acc.get_balance())
    print("-----------------------")

    t = Temperature(25)
    print("F: ", t.fahrenheit)
    t.fahrenheit = 212
    print("C: ", t.get_celsius())


if __name__ == "__main__":
    main()

