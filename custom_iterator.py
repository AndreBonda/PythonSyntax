# La maggior parte dei contenitori di oggetti in Python è iterabile in modo similare.

for e in [1,2,3]:
    print(e)

for e in (1,2,3):
    print(e)

for e in "123":
    print(e)

# Un oggetto iterabile implementa il metodo iter()
# iter(): che restituisce un iteratore che implementa il metodo __next__()

class Reverse:
    def __init__(self, data) -> None:
        self.data = data
        self.index = len(data) - 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < 0:
            self.index = len(self.data) - 1
            raise StopIteration

        res = self.data[self.index]
        self.index -= 1
        return res

rev = Reverse("abc")

# c b a
for c in rev:
    print(c)