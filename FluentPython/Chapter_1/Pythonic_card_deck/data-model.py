import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list("JQKA")
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDeck()
print(len(deck)) # 52
print(deck[0]) # Card(rank='2', suit='spades') -> Equivale a print(deck.__getitem__(0))

# pick random card
randomCard = choice(deck)
print(randomCard)

randomCard = choice(deck)
print(randomCard)

# first n cards
print(deck[:3])

# iterable
for card in deck[10:20]:
    print(card)

print(Card('Q', 'hearts') in deck) # True
print(Card('Q', 'wrong_suit') in deck) # False

# implementare un sistema di ranking
print("\nSorting----------")
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

# Esempio ranking delle carte
# 2 - 'clubs' -> 0
# 2 - 'diamond' -> 1
# 2 - 'hearts' -> 2
# 2 - 'spades' -> 3
# 3 - 'clubs' -> 4
# ...
# A - 'hearts' -> 50
# A - 'spades' -> 51
def card_rank(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=card_rank):
    print(card)
