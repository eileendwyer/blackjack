from itertools import product
import random


class Deck:

    def __init__(self):
        self.suit = 'SCDH'
        self.rank = 'A23456789TJQK'
        self.cards = tuple(''.join(card) for card in product(self.rank, self.suit))
        self.deck = random.sample(self.cards, 52)


    def shuffle(self):
        return deck.shuffle()

deck = Deck()
#print(deck.deck)
