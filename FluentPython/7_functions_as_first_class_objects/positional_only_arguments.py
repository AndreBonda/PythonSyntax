# All arguments to the left of / are positional-only. After the /, you may specify all 
# other arguments, which work as usual

def div_and_mod(a, b, /):
    return (a // b, a % b)

result = div_and_mod(4, 3)
print(result) # (1, 1)