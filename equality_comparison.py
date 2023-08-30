import heapq

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
    
a = [1,2,3]
b = [1,2,3]
print(a == b) # True

p1 = Person("Andrea")
p2 = Person("Andrea")
print(p1 == p2) # False

pset = set()
pset.add(p1)
pset.add(p2)

for p in pset: # Andrea, Andrea
    print(p)

p1 = PersonComp("Luca")
p2 = PersonComp("Luca")
print(p1 == p2) # True

pset = set()
pset.add(p1)
pset.add(p2) # ignored because p1 is equal to p2

for p in pset: # Luca
    print(p)

# Sorting elements with lamba function
print("-------")
people = [PersonComp("Andrea"), PersonComp("Luca"), PersonComp("Antonio"), PersonComp("Claudio")]
for p in people:
    print(p)

print("-------")
people.sort(key=lambda p: p.name)

for p in people:
    print(p)

# min-heap with people
class SortablePeople:
    def __init__(self, name):
        self.name = name
    
    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.name == other.name

    def __repr__(self) -> str:
        return self.name

    def __lt__(self, other): # lt --> less than
        return self.name < other.name
    
    

print('----- Sortable peole')
people = [SortablePeople("Andrea"), SortablePeople("Luca"), SortablePeople("Antonio"), SortablePeople("Claudio")]
people.sort()
for p in people:
    print(p)

# definendo lt posso utilizzare anche heapq
print('-----HEAPQ')
people = []
heapq.heappush(people, SortablePeople("Andrea"))
heapq.heappush(people, SortablePeople("Luca"))
heapq.heappush(people, SortablePeople("Antonio"))
heapq.heappush(people, SortablePeople("Claudio"))
heapq.heappush(people, SortablePeople("Andrea"))
heapq.heappush(people, SortablePeople("Claudio"))

while people:
    print(heapq.heappop(people)) # popping in order