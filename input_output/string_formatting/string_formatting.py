import math

# rounding
print(f'The value of pi is approximately {math.pi:.3f}')
print(f'The value of pi is approximately {round(math.pi, 3)}')

# minimum number characters wide. 
# I valori in questo caso occupano almeno 10 caratteri
table = {"Andrea": 5463, "Luca": 9834, "Marco": 5642}

for name, phone in table.items():
    print(f"{name:10}=>{phone:10}")

# string.format
print("{} and {}".format("fast", "furious")) # fast and furious

# string format ordering
print("{1} and {0}".format("fast", "furious")) # furious and fast

# string format keyword arguments
print("This {food} is {adjective}".format(food="pizza", adjective="amazing"))