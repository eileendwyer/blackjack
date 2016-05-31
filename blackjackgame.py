# welcome player
# start game

from itertools import product
import random


def blackjack_game():
    print("Let's play Blackjack!\n The House Rule is the dealer will stand on 17.\n"
          "The Dealer is shuffling the deck.")
    player = print("Player")
    dealer = print("Dealer")
    Dealer()
# make deck
# shuffle deck
# deal a hand, 2 cards
# deal a hit, 1 card
# remove cards at end of game

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

    def shuffle(self):
        return self.shuffle_deck


    def deal_hit(self):
        hit = self.card
        self.hand.append(hit)
        return self.hand


    def deal_hand(self):
        deal = self.first_deal
        self.hand.append(deal)
        return self.hand

    def clear_hand(self):
        self.hand = []
        self.hand_value = 0


class Hand(Dealer):

    def __init__(self):
        super(Dealer).__init__()  # inheriting all from dealer
        self.deck_value = {card: min(1 + self.rank.index(card[0]), 10) for card in self.deck}
        self.hand_value = 0
        self.player = Player

    def value_hand(self):
        for card in self.hand:
            count_aces = 0
            #count_aces = [ += 1 for card in self.hand if card[1] == 'A']
            if card[1] == 'A':
                count_aces += 1
                self.hand_value += self.deck_value[card[1]]
            if count_aces > 0 and self.hand_value < 12:
                self.hand_value += 10
        return self.hand_value

    def play_hand(self, dealer):
        dealer.value_hand()
        if dealer.value_hand <= 16:
            dealer.deal_hit()
        elif dealer.value_hand >= 17:
            print("Dealer stays.")
            print(dealer.hand_value)
        else:
            if dealer.value_hand == 21:
                print("Dealer wins with 21!")
                dealer.clear_hand()
        return dealer.value_hand

    def end_game(self):
        play_again = input("Do you want to play again? y/n").lower()
        if play_again == 'y':
            shuffle()
            deal_hand()
        else:
            print("Goodbye!")


class Player(Hand):

    def __init__(self):
        self.player = Player

        def play_hand(self, player):
            Player.value_hand()
            while Player.value_hand < 21:
                hit_stay = input("Hit or stay? h/s").lower()
                if hit_stay == 'h':
                    self.deal_hit
                else:
                    if (self.player.value_hand > dealer.value_hand) or (dealer.value_hand > 21):
                        print("You win!")
            clear_hand()
            end_game()


def game():
    blackjack_game()

blackjack_game()
Dealer()
Hand()
Player()
# hand = Dealer()
# print(hand.deal_hand())
# card = Dealer()
# print(card.deal_hit())

