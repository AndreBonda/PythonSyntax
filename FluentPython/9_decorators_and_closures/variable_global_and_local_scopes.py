def f1(a):
    print(a) # 3
    print(b) # 5

b = 5
f1(3)

print('---------')

def f2(c):
    global d
    print(c) # 6
    # Se non dichiarassi la variabile 'd' come global, qui andrebbe in errore poiché alla riga dopo c'è una assegnazione della variabile 'd', quindi Python la vedrebbe come una variabile locale. 
    # Quando prova a stamparla lancierebbe un errore poiché non è stata ancora assegnata. (UnboundLocalError: cannot access local variable 'd' where it is not associated with a value)
    print(d) # 10
    d = 4

d = 10
f2(6)
print(d) # 4