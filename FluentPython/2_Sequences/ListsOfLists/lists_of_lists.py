# Esempio di inizializzazione matrice
rows = 3
cols = 5
board = [['_'] * cols for i in range(rows)]
board[1][2] = 'X'
print(board)

# Alternativa
board = []

print("---")
for r in range(rows):
    row = ['_'] * cols
    board.append(row)
board[2][2] = 'X'
print(board)