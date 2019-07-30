class Account:

    def __init__(self,filepath):
        self.filepath=filepath
        with open(self.filepath, mode='r') as file:
            self.balance=int(file.read())

    def withdraw(self,amount):
        self.balance=self.balance - amount

    def deposit(self,amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class Checking(Account):
    """This class generates checking account objects"""

    type = "Checking"

    def __init__(self,filepath,fee):
        Account.__init__(self,filepath)
        self.fee=fee

    def transfer(self,amount):
        self.balance=self.balance - amount - self.fee

# account=Account("balance.txt")
# print(account.balance)
# account.withdraw(100)
# account.commit()
# print(account.balance)
# account.deposit(200)
# account.commit()
# print(account.balance)

jack_checking=Checking("jack.txt",1)

jack_checking.transfer(100)
jack_checking.commit()
print(jack_checking.balance)
print(jack_checking.type)

print(jack_checking.__doc__)
