# Dovresti evitare oggetti mutable come valori di default dei parametri passati alle funzioni

class BadImplementationBus:
    # assegnare [] come valore di default porta a comportamenti indesiderati se passengers non viene passato.
    # In questo caso 'self.passengers' diventa un alias per la default list. Quando vengono chiamati i metodi .remove e .append stiamo modificando la default list.
    def __init__(self, passengers=[]) -> None:
        self.passengers = passengers
    
    def pick(self, name):
        self.passengers.append(name)
    
    def drop(self, name):
        self.passengers.remove(name)

class Foo:
    def __init__(self, passengers=[]) -> None:
        self.passengers = passengers

b1 = BadImplementationBus(['Alice', 'Bill'])
print(b1.passengers) #['Alice', 'Bill']
b1.pick('Charlie')
b1.drop('Alice')
print(b1.passengers) #['Bill', 'Charlie']

b2 = BadImplementationBus()
b2.pick('Carrie')
print(b2.passengers) #['Carrie']

b3 = BadImplementationBus()
print(b3.passengers) #['Carrie']

class GoodImplementationBus:
    def __init__(self, passenger = None) -> None:
        if passenger is None:
            self.passenger = []
        else:
            self.passenger = list(passenger) # in questo modo eseguo una copia del parametro in modo tale che non propargo le modifiche al di fuori della classe.