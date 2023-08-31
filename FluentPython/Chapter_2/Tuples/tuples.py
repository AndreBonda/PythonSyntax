# Tuples are sequence data type like strings and arrays. Tuples are immutables.

# tuple packing
t = 1995, "Andrea", "Bondanini" # oppure t = (val1, val2, ...)
print(t)
print(t[0])

# nested tuples
t = (5,"Giugno"), "Andrea"
print(t)

# tuples are immutable but can contain mutable objects
t = ([1,2],[3,4])
t[0][0] = 0
print(t) # ([0, 2], [3, 4])

# empty tuple
t = ()
print(t) # ()

# tuple with 1 value.
t = ("Hello",) # comma is needed
print(t)

# namedtuple
# Utili per creare oggetti che sono un insieme di attributi senza custom methods (record)
import collections

Employee = collections.namedtuple("Employee", ['name', 'surname'])
bestEmployee = Employee("Andrea", "Bondanini")
print(bestEmployee) # Employee(name='Andrea', surname='Bondanini')