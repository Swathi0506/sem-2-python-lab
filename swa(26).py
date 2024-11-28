#1.
class BankAccount:
    def __init__(self, name, account_number, balance=3000):
        self.name = name
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        if amount>0:
            self.balance += amount
            print(f"Deposited: {self.balance}")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {self.balance}")
        else:
            print("Not enough balance!")
    def check_balance(self):
        print(f"Balance: {self.balance}")
obj1=BankAccount("Swathi","2345678901",3000)
obj1.deposit(2000)
obj1.withdraw(2000)
obj1.check_balance()

#2.
class Cosmetics:
    def __init__(self,p_name="Lakmekajal",p_brand="Lakme",p_cost=250,p_cat="Eye makeup"):
        self.p_name=p_name
        self.p_brand=p_brand
        self.p_cost=p_cost
        self.p_cat=p_cat
    def display(self):
        print("Product_Name--",self.p_name)
        print("Product_Brand--",self.p_brand)
        print("Product_cost--",self.p_cost)
        print("Product_category--",self.p_cat)
obj=Cosmetics()#if we provide the values it will execute the values which we provide at last not a default values
obj.display()
