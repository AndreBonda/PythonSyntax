# List comprehensions are concise ways to create lists







# flatten a list
lists = [[1,2,3], [4], [5,6,7]]
flat = [x for l in lists for x in l]
print(flat) # [1, 2, 3, 4, 5, 6, 7]

# traspose a matrix 3*4
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

traspose = [[row[i] for row in matrix] for i in range(4)]
print(traspose)
# è presente anche una funzione built-in in python => traspose = list(zip(*matrix))
