import random

class Person:
    '''Simple class'''

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        self.__id = random.randint(0,100)
    
    def sayHello(self):
        print(f"Hi, I'm {self.name}. I'm {self.age}")
    
    def myId(self):
        print(f"My id is {self.__id}")

p = Person("Andrea", 28)
p.age = 19
p.sayHello() # self è l'istanza che viene passata come parametro --> Person.sayHello(p)
print(Person.__doc__)

# Inheritance
class Employee(Person):

    def __init__(self, name, age, role) -> None:
        super().__init__(name, age)
        self.role = role
    
    def __repr__(self) -> str:
        return f"{self.name} - {self.age} - {self.role}"
    
    def sayHello(self):
        super().sayHello() # Person.sayHello(self)
        print("I'm an employee")

sde = Employee("Luca", 35, "Software developer engineer")
print(sde)
# sde._Person__id = 76 -> per accedere agli attributi privati
sde.sayHello()
sde.myId()