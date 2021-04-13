class User:
    def users(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
            self.deposit(amount)
            return self


    def make_withdrawl(self, amount):
            self.withdrawl(amount)
            return self


    def display_user_account_info(self):
        self.name
        self.email
        return self


    def yeild_interest(self):
        returns = self.balance*self.int_rate
        self.balance += returns
        return self



george = ("George Michaels", "gm@email.com")
jimmy = ("jimmy john", "jj@email.com")




print(jimmy.display_usesr_account_info)




