# Use lambda keyword for anonymous functions
pairs = [(1, "one"), (5, "five"), (7, "seven")]
pairs.sort(key=lambda p: p[1]) # sort by string
print(pairs) # [(5, 'five'), (1, 'one'), (7, 'seven')]