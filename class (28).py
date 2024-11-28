#1
class Inventory:
    def _init_(self,prodId,prodName,prodCount):
        self.prodId=prodId
        self.prodName=prodName
        self.prodCount=prodCount
    def display(self):
        print("Product ID=",self.prodId)
        print("Product Name=",self.prodName)
        print("Product Count=",self.prodCount)
obj=Inventory("A1234","Lakme",4)
obj.display()

#2
class Inventory:
    def _init_(self,prodId,prodName,prodCount):
        self.prodId=prodId
        self.prodName=prodName
        self.prodCount=prodCount
    def display(self):
        print("Product ID=",self.prodId)
        print("Product Name=",self.prodName)
        print("Product Count=",self.prodCount)
class Todisplay(Inventory):
    def getdet(self):
        self.display()
obj=Todisplay("A1234","Lakme",4)
obj.getdet()

#3.
class Employee:
    def getEmployeeInfo(self):
        self.id=input("Enter the ID")
        self.name=input("Enter the name:")
    def displayEmployeeInfo(self):
        print("ID=",self.id,"\n Name=",self.name)
class Perks(Employee):
    def getDetails(self):
        self.getEmployeeInfo()
        self.sal=int(input("Enter the salary:"))
    def displayInfo(self):
        self.displayEmployee()
        print("salary=",self.sal)
p=Perks()
p.getDetails()
p.displayInfo()
