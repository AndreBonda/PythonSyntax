# Una Closure è una funzione 'f' con uno scope esteso che comprende riferimenti a variabili (non globali) che sono denifite nello scope di una outer-function 'd'
# che comprende la funzione 'f'.

# Esempio
# Considera una funzione 'avg' che calcola la media di una serie di valori che continua a crescere nel tempo.

# Implementazione con una classe
class Averager:
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        return sum(self.series) / len(self.series)

# Implementazione funzionale. In questo caso la funzione averager è la closure, che tiene riferimenti alla variabile 'series'
def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        return sum(series) / len(series)

    return averager

avg = Averager()
print(avg(10)) # 10.0
print(avg(11)) # 10.5
print(avg(12)) # 11.0

print('-----')

avg = make_averager()
print(avg(10)) # 10.0
print(avg(11)) # 10.5
print(avg(12)) # 11.0

# I riferimenti alle "free variables", ovvero le variabili non definite nello scope locale sono mantenuti in "avg.__code__.co_freevars"
print(avg.__code__.co_freevars) # ('series',)

# Possiamo migliorare l'implementazione di make_averager in modo date che non calcoli la media ad ogni chiamata.

def make_averager_v2():
    total = 0
    count = 0

    def averager(new_num):
        nonlocal total, count

        total += new_num
        count += 1
        return total / count

    return averager

# Questa volta devo dichiarare le variabili che voglio modificare come nonlocal, altrimenti riceverei un errore essendo non ancora assegnate.
# Nell'implementazione di prima non era necessario poiché series è una lista ed essendo mutabile e non veniva riassegnata.