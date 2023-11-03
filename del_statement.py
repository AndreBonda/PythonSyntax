# Del statement offers a way to delete item from a list given its index

# delete single element
l = [-2,-1,1,2,5,8,9]
del l[0]
print(l) # [-1, 1, 2, 5, 8, 9]

# delete slice
l = [-2,-1,1,2,5,8,9]
del l[1:3] # elimina elemento in posizione 1 e 2
print(l) # [-2, 2, 5, 8, 9]

# delete all elements
l = [-2,-1,1,2,5,8,9]
del l[:]
print(l) # []

# delete a variable. You can't reference it after this instruction.
# Tecnincamente è sbagliato dire che stiamo eliminando l'array, poiché in realtà stiamo eliminando la variabile 'l'. L'array verrà eliminato di conseguenza dal GC se nessun altra
# variabile è "bindata" all'array.
l = [-2,-1,1,2,5,8,9]
del l
# print(l) -> It throws 'NameError: name 'l' is not defined'