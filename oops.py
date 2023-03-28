# Square Numbers and Return Their Sum

class point:
    def __init__(self,x,y,z):
     self.x=x*x
     self.y=y*y
     self.z=z*z
    def display(self):
        print("sqsum:",self.x+self.y+self.z)
        
obj=point(1,3,5)
obj.display()

#2 implement a class calculator:
class Calculator:
    
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num2 - self.num1
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        if self.num1 == 0:
            return "Error: Cannot divide by zero"
        else:
            return self.num2 / self.num1
obj = Calculator(10, 94)
print(obj.add()) 
print(obj.subtract())
print(obj.multiply()) 
print(obj.divide())

#3)implement a student class
class Student:
    
    def __init__(self):
        self.__name = ""
        self.__rollNumber = ""
        
    def setName(self, name):
        self.__name = name
        
    def getName(self):
        return self.__name
    
    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber
        
    def getRollNumber(self):
        return self.__rollNumber
s = Student()
s.setName("John")
s.setRollNumber("1234")
print(s.getName()) 
print(s.getRollNumber())

#4)Implement a Banking Account
class Account:
    
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate
a = Account("Ashish", 5000)
print(a.title) 
print(a.balance) 

s = SavingsAccount("Ashish", 5000, 5)
print(s.title) 
print(s.balance) 
print(s.interestRate)    

#5)Handling a Bank Account
class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def withdrawal(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount
        
    def getBalance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate
    
    def interestAmount(self):
        return (self.balance * self.interestRate)/100

demo1 = SavingsAccount("Ashish", 2000, 5)
demo1.deposit(500)
print(demo1.getBalance())   
demo1.withdrawal(500)
print(demo1.getBalance())   
print(demo1.interestAmount())   