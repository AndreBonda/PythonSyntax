# List comprehensions are concise ways to create lists

squares = [x**2 for x in range(10)]
print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

cross_results = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(cross_results) # [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

positives = [x for x in [-2,-1,0,1,2,3] if x > 0]
print(positives) # [1,2,3]

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
