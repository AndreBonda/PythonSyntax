# Arrays (called lists in python)
arr = [1,2,3]
print(arr[0])

# Array sono dynamic di default, quindi utilizzabili come stack
arr.append(4)
arr.append(5)
popped = arr.pop()

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