
class BankAccount:
    def __init__(self, name, email):
        self.int_rate = 0.01
        self.balance = 0
        self.name = name
        self.email = email
        

    def deposit(self, amount):
        self.balance += amount
        return self


    def withdrawl(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print("Insufficient funds: Charging a $5 fee.")
            self.balance -5
        return self


    def display_account_info(self):
        self.name
        self.email
        return self


    def yeild_interest(self):
        returns = self.balance * self.int_rate
        self.balance += returns
        return self

blake = BankAccount( "blake gifford", "blake@email.com")
john = BankAccount( "john john", "john@email.com")
jordan = BankAccount( "jordan george", "jordan@email.com")

blake.deposit(1000).deposit(1000).deposit(1000).withdrawl(505)

jordan.deposit(22).deposit(3425).withdrawl(37).withdrawl(832328).withdrawl(1)

print(blake.balance)
print(jordan.balance)

