from array import array
from random import random

# quando si inizializziano gli array si dichiara il typecode per dichiarare il tipo di dato e ottimizzare le performance
bts = array('b', (-128, 127)) # dichiarando il typecode 'b', abbiamo un array di byte. Ogni valore che cerchiamo di inserire fuori dal range -128 +127 causera un OvreflowError
print(bts)

# 'd' typecode for double precision floating point
# 10 ^ 2
floats = array('d', (random()for i in range(10**2)))
print(floats)