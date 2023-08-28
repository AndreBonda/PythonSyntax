#----- List comprehensions
# List comprehensions (listcomps) are concise ways to create lists increasing the readability
squares = [x**2 for x in range(10)]
print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Listcomps ci permettono di scrivere in modo più semplice senza l'utilizzo di funzioni ulteriori
# come map e filter
symbols = "abc%&/d1"
ascii = [ord(c) for c in symbols if ord(c) > 56] # => ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(ascii) # [97, 98, 99, 100]

# Listcomps utili per il prodotto cartesiano sugli iterables. Genera una list di tuple
colors = ['red', 'blue']
sizes = ['S', 'M', 'L']
tshirts = [(c,s) for c in colors for s in sizes]
print(tshirts) # [('red', 'S'), ('red', 'M'), ('red', 'L'), ('blue', 'S'), ('blue', 'M'), ('blue', 'L')]

cross_results = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(cross_results) # [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

positives = [x for x in [-2,-1,0,1,2,3] if x > 0]
print(positives) # [1,2,3]

#----- Generator expressions
# stessa sintassi delle list comprehensions ma racchiuse tra parentesi tonde
symbols = "abc%&/d1"
t = tuple(ord(s) for s in symbols)
print(t) # (97, 98, 99, 37, 38, 47, 100, 49)

colors = ['red', 'blue']
sizes = ['S', 'M', 'L']

# a differenza della listcomp sopra, in questo caso non viene creata nessuna lista contenente il prodotto cartesiano di colors e sizes.
# Viene creato un elemento per volta. (migliori performances)
for tshirt in (f'{c} {s}' for c in colors for s in sizes):
    print(tshirt)