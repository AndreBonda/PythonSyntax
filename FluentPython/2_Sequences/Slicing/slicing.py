l = [10,20,30,40,50,60]
part_one = l[:2]
part_two = l[2:]
print(part_one) # [10, 20]
print(part_two) # [30, 40, 50, 60]

# prendi i caratteri dopo ogni step n
n = 3
s = "bycicle"
print(s[::n]) # bie

# la sintassi [start:stop:step] crea un oggetto slice(start, stop, step)
line = "05-06-1995.Andrea.Bondanini"
data = slice(0,10) # 05-06-1995
name = slice(11,17) # Andrea
surname = slice(18, 29) # Bondanini

print(line[data])
print(line[name])
print(line[surname])

# reverse a string
print(s[::-1])

# slicing for modify a sequence
l = list(range(10))
print(l) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l[2:5] = [0,0,0]
print(l) # [0, 1, 0, 0, 0, 5, 6, 7, 8, 9]