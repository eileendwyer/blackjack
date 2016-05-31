from itertools import product
from random import sample
import random

def blackjack_game():
    print("Let's play Blackjack!\n The House Rule is the dealer will stand on 17.")
    start_game = Dealer()


class Dealer:

    def __init__(self):
        self.suit = 'SCDH'
        self.rank = 'A23456789TJQK'
        self.deck = tuple(''.join(card) for card in product(self.rank, self.suit))
        self.shuffle_deck = random.sample(self.deck, 52)
        self.card = self.shuffle_deck[-1]
        self.first_deal = self.shuffle_deck[-1], self.shuffle_deck[0]
        self.hand = []
        self.hand_value = 0


    def deal_hit(self):
        hit = self.card
        self.hand.append(hit)
        return self.hand


    def deal_hand(self):
        self.first_deal = self.shuffle_deck[-1], self.shuffle_deck[0]
        self.hand.append(self.first_deal)
        return self.hand

    def clear_hand(self):
        del self.hand[:]
        del self.hand_value[:]












def game():
    blackjack_game()
    # hand = Dealer()
    # print(hand.deal_hand())
    # card = Dealer()
    # print(card.deal_hit())