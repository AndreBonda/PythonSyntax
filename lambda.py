# importing the random module
import random

def make_incrementator(base):
    return lambda x: base + x

f = make_incrementator(50)

print(f(1)) # 51
print(f(2)) # 52

# pass function as a parameter
def age_random():
    return random.randint(0,99)

def say_hello(rand):
    return f"Hello, Andrea's here. I'm {rand()}"

print(say_hello(age_random))

# use lambda function to pass a small function as a parameter
pairs = [(1, "one"), (5, "five"), (7, "seven")]
pairs.sort(key=lambda p: p[1]) # ordina in base alla stringa
print(pairs) # [(5, 'five'), (1, 'one'), (7, 'seven')]