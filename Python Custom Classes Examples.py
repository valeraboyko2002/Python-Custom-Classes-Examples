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
