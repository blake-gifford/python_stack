
class user:
    def __init__(self, name):
        self.name = name
        self.account_balance = 1000
    def account_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def account_deposit(self, amount):
        self.account_balance += amount
        return self
blake = user("blake gifford")
john = user("john john")
jordan = user("jordan georg")

blake.account_deposit(4532).account_deposit(45).account_deposit(532).account_withdrawal(250)

john.account_deposit(6464).account_deposit(64).account_withdrawal(664).account_withdrawal(998.99)

jordan.account_deposit(45958.37).account_withdrawal(459.57).account_withdrawal(458).account_withdrawal(.67)

print(blake.account_balance)
print(john.account_balance)
print(jordan.account_balance)