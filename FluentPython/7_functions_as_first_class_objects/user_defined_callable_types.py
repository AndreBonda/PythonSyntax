# Arbitrary Python objects can be made "callable" objects implementing __call__ instance method.

import random

class BingoCage:
    def __init__(self, items) -> None:
        self._items = list(items)
        random.shuffle(self._items)
    
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')
    
    def __call__(self):
        return self.pick()

bingo = BingoCage(range(5))
print(bingo.pick()) # <a random number>
print(bingo()) # <a random numnber>

