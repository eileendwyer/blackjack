from itertools import product
import random


class Dealer:

    def __init__(self):
        self.suit = 'SCDH'
        self.rank = 'A23456789TJQK'
        self.cards = tuple(''.join(card) for card in product(self.rank, self.suit))
        self.deck = random.sample(self.cards, 52)
        self.card = self.deck[-1]
        self.first_deal = self.deck[-1], self.deck[0]
        self.hand = []

    def shuffle(self):
        return deck.shuffle()

    def deal_hit(self):
        hit = self.card
        self.hand.append(hit)

    def deal_hand(self):
        deal = self.first_deal
        self.hand.append(deal)
#        return self.hand

    def clear_hand(self):
        self.hand = []
        self.hand_value = 0

deal = Dealer()
# print(deal.first_deal)
hit = Dealer()
# print(hit.card)
deck = Dealer()
# print(deck.deck)