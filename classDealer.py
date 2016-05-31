from deck import Deck
deck = Deck()
class Dealer:

    def __init__(self):
        self.deck = random.sample(self.cards, 52)
        self.card = self.deck.pop()
        self.first_deal = []
        self.hand = []

    def deal_hit(self):
        self.hand.append(self.card)
#        self.card.deal_hit()
#        return self.hand
card = Dealer()
print(card.card)






"""
    def deal_hand(self):
        self.first_deal = self.shuffle_deck[-1], self.shuffle_deck[0]
#        self.hand.append(self.first_deal)
#        self.hand.deal_hand()

first_hand = Dealer()
print(first_hand.first_deal)
    def clear_hand(self):
        del self.hand[:]
        del self.hand_value[:]

def blackjack_game():
    print("Let's play Blackjack!\n The House Rule is the dealer will stand on 17.")

blackjack_game()
# hand = Dealer()
# print(hand.deal_hand())
"""


