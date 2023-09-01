# list
a = [1,2,3]
b = list()
b.append(1)
b.append(2)
b.append(3)

print(a)
print(b)

# list sono dynamic di default, quindi utilizzabili come stack
a.append(4)
a.append(5)
popped = a.pop()
print(popped) # 5
print(4 in a) # True

# Insert
a.insert(1, 7) # inserisce 7 in posizione 1 --> O(N)
print(a) # [1, 7, 2, 3, 4]

# Inizializza un array di size n con i valori di default a 1
n = 5
arr = [1] * 5
print(arr) # [1, 1, 1, 1, 1]

# -1 non è out of bounds ma l'ultimo valore
arr = [1, "abc", "cde"]
print(arr[-1]) # cde
print(arr[-2]) # second last value --> abc

# Sublists (aka slicing)
arr = ["a","b","c","d"]
print(arr[1:4]) # stampa da posizione 1 compresa a 4 (non compresa)

# 2-D lists --> matrice 5x4 inizializzata a 0
arr = [[0] * 4 for i in range(5)]
print(arr) # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# max
print("max")
arr = [1,2,3]
print(max(arr))

# Comparing arrays
print("--- Array comparison ---")
arr1 = [1,2,3]
arr2 = [1,2,3]
print(arr1 == arr2) # True

arr1 = [1,2,3]
arr2 = [1,2,4]
print(arr1 == arr2) # False

# Convert string to char array
print("--- Convert string to char array ---")
string = "andrea"
arr = [char for char in string]
print(arr) # ["a","n","d","r","e","a"]

# list concat
print([1,2,3]+[4,5,6]) # -> 1,2,3,4,5,6

# ===== List methods
l = [1,2,3]
l.append(4)
print(l) # 1,2,3,4

l = [1,2,3]
l.extend([4,5])
print(l) # 1,2,3,4

l = [1,2,3]
l.insert(1,5)
print(l) # 1,5,2,3

l = [10,20,30]
l.remove(20)
print(l) # 10,30

l = [1,2,3]
popped = l.pop()
print(popped) # 3
print(l) # 1,2

l = [10,20,30]
popped = l.pop(1)
print(popped) # 20
print(l) # 10,30

l = [10,20,30]
l.clear()
print(l) # []

l = [10,20,30,40,50]
l = l.index(20) # resituisce l'indice del numero -> 1
print(l)

l = [10,20,30,40,50]
l = l.index(20, 0, 3) # resituisce l'indice del numero cercando in un range compreso tra l'indice 0 e 3 -> 1
print(l)

l = [1,1,2,3]
print(l.count(1)) # 2

# Sorting in place
l = [5,3,7,8,1]
l.sort() # in place sorting
print(l) # 1,3,5,7,8

# Sorting and return new list
print("--- sorting and return new list")
a = [3,1,2]
b = sorted(a)
print(a) # [3,1,2]
print(b) # [1,2,3]

# Sorting parameters (funziona sia con sorted(list) che con list.sort())
print("--- sorting and parameters")
# Reversing sort
l = [1,2,3]
l.sort(reverse=True)
print(l)
# Sorting by key
names = ['Bob', 'Alan', 'Xi', 'Giangiacomo']
names.sort(key=len)
print(names) # ['Xi', 'Bob', 'Alan', 'Giangiacomo']


l = [1,2,3]
l2 = l.copy() # swallow copy - alternativa l2 = l[:]
print(l2) # 1,2,3

# shuffle elements
import random
l = [1,2,3,4,5,6,7]
random.shuffle(l)
print(l)

# Add lists
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c) # [1, 2, 3, 4, 5, 6]

# Multiply lists
m = [1] * 5
print(m) # [1, 1, 1, 1, 1]

# Augmented assignment operators (+= o *=)
# Lo speciam method che viene invocato è __iadd__ (oppure __imul__ per l'operatore *). Se __iadd__ non è implementato viene invocato __add__ come fall back
# Il comportamento dipende dal tipo di operando su cui eseguiamo l'augmented assignment

# mutable sequence
l = [1,2,3]
print(id(l))
l *= 2
print(id(l)) # id rimane il medesimo poiché l'oggetto viene modificato in place

# immutable sequences
t = (1,2,3)
print(id(t))
t *= 2
print(id(t)) # id cambia poiché essendo una immutable sequence, t referenzia un nuovo oggetto