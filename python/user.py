
class user:
    def __init__(self, name):
        self.name = name
        self.account_balance = 1000
    def account_withdrawal(self, amount):
        self.account_balance -= amount
    def account_deposit(self, amount):
        self.account_balance += amount
blake = user("blake gifford")
john = user("john john")
jordan = user("jordan georg")
blake.account_deposit(4532)
blake.account_deposit(45)
blake.account_deposit(532)
blake.account_withdrawal(250)

john.account_deposit(6464)
john.account_deposit(64)
john.account_withdrawal(664)
john.account_withdrawal(998.99)

jordan.account_deposit(45958.37)
jordan.account_withdrawal(459.57)
jordan.account_withdrawal(458)
jordan.account_withdrawal(.67)

print(blake.account_balance)
print(john.account_balance)
print(jordan.account_balance)