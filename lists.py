# Arrays (called lists in python)
arr = [1,2,3]
print(arr[0])

# Array sono dynamic di default, quindi utilizzabili come stack
arr.append(4)
arr.append(5)
popped = arr.pop()

print(4 in arr)

print(popped)
print(arr)

# Insert
arr.insert(1, 7) # inserisce 7 in posizione 1 --> O(N)
print(arr)

# Inizializza un array di size n con i valori di default a 1
n = 5
arr = [1] * 5
print(arr)
print(len(arr))

# -1 non è out of bounds ma l'ultimo valore
arr = [1, "abc", "cde"]
print(arr[-1]) # cde
print(arr[-2]) # second last value --> abc

# Sublists (aka slicing)
arr = ["a","b","c","d"]
print(arr[1:4]) # stampa da posizione 1 compresa a 4 (non compresa)

# Unpacking
a, b, c = [1, 2, 3]
print(a, b, c)

# 2-D lists --> matrice 5x4 inizializzata a 0
arr = [[0] * 4 for i in range(5)]
print(arr)

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

l = [5,3,7,8,1]
l.sort()
print(l) # 1,3,5,7,8
l.sort(reverse=True) # list.reverse()
print(l) # 8,7,5,3,1

l = [1,2,3]
l2 = l.copy() # swallow copy - alternativa l2 = l[:]
print(l2) # 1,2,3
