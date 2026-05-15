class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f'{self.name} is crying!')

# ---Object---

dog1 = Dog('Bob', 3)
dog2 = Dog('Joky', 5)

dog1.bark()
dog2.bark()

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self , amount):
        self.balance += amount

    def show_balance(self):
        print(self.owner, 'has', self.balance)

# Use it ---------

acc1 = BankAccount('Million', 1000)

acc1.deposit(500)
acc1.show_balance()

# Connecting to Logging filter---------
class OnlyEven:
    def check(self, number):
        return number % 2 == 0

# let's use it-----
f = OnlyEven()
print(f.check(4))
print(f.check(5))

class PassOrFail:
    def check(self, mark):
        if mark >= 50:
            return "Pass"
        else:
            return "Fail"

p = PassOrFail()
print(p.check(70))
print(p.check(30))


def check(mark):
    if mark >= 50:
        return 'Pass' if mark >= 50 else 'Fail'

print(check(70))
print(check(30))