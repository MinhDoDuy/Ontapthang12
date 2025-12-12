class BankAccount():
    def __init__(self, balance = 0):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit amount: {amount}, New balance: {self.__balance}")
        else:
            print("Amount must be > 0")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be > 0")
        elif amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print(f"Withdraw {amount}. New balance: {self.__balance}")

    def get_balance(self):
        return self.__balance


class Temperature():
    def __init__(self, celsius = 0):
        self.__celsius = celsius

    @property
    def fahrenheit(self):
        return (self.__celsius * 9 / 5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        # chuyển Fahrenheit -> Celsius
        self.__celsius = (value - 32) * 5 / 9

    def get_celsius(self):
        return self.__celsius