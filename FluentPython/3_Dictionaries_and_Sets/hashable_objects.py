class Person:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self) -> str:
        return self.name

class PersonComp:
    def __init__(self, name):
        self.name = name
    
    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.name == other.name

    def __repr__(self) -> str:
        return self.name

print("----- No comparable person -----")
p1 = Person("Andrea")
p2 = Person("Andrea")
print(p1 == p2) # False

pset = set()
pset.add(p1)
pset.add(p2)

print(pset) # {Andrea, Andrea}

print("----- Comparable person -----")
p1 = PersonComp("Luca")
p2 = PersonComp("Luca")
print(p1 == p2) # True

pset = set()
pset.add(p1)
pset.add(p2) # ignored because p1 is equal to p2

print(pset) # {Luca}