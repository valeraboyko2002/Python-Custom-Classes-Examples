class TypedList(list):
    
    def __init__(self, element_type=int):
        self.element_type = element_type
        super().__init__() 
    
    def append(self, item):
        if isinstance(item, self.element_type):
            super().append(item)
        else:
            raise TypeError("Ошибка типа")

l = TypedList(element_type=str)
l.append("Привет")
print(l)  

l.append(8) # ошибка типа 

# _____________________________________________________________________________________________________
class My_List(list):

    def sum_odd(self):
        return sum([x for x in self if x % 2 == 1])
    
    def sum_even(self):
        return sum([x for x in self if x % 2 == 0])

l = My_List([1,2,3,4,5,6,7,8,9,10])
l.sum_even()
l.sum_odd()

# _____________________________________________________________________________________________________
class Email:
    
    domain = "github.com"

    def adress(self):
        return self.name + "@" + self.domain
    
class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age 

class Unit:
    
    def __init__(self,name):
        self.name = name 

class Employee(Person,Email):

    pass

class Organization_Unit(Unit,Email):
    pass

a = Employee("Valera",22)
a.adress()
b = Organization_Unit("Biba")
b.adress()

# _________________________________________________________________________________________________________

class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder  
        self.__balance = initial_balance  
        self.__transactions = []  
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        self.__balance += amount
        self.__transactions.append(f"Пополнение: +{amount}")
        return f"Пополнено {amount}. Баланс: {self.__balance}"
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        if amount > self.__balance:
            raise ValueError("Недостаточно средств")
        self.__balance -= amount
        self.__transactions.append(f"Снятие: -{amount}")
        return f"Снято {amount}. Баланс: {self.__balance}"
    
    @property
    def balance(self):
        return self.__balance

    def get_transactions(self):
        return self.__transactions.copy()  
    
    @property
    def account_holder(self):
        return self.__account_holder
    
    @account_holder.setter
    def account_holder(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Имя владельца должно быть непустой строкой")
        self.__account_holder = value



account = BankAccount("Иван Иванов", 1000)
print(account.deposit(500))  
print(account.withdraw(200)) 
# account.__balance = 10000  # Ошибка! Приватное поле
print(f"Баланс: {account.balance}")  
