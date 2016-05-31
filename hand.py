from dealer import Dealer
import random

def blackjack_game():
    print("Let's play Blackjack!\n The House Rule is the dealer will stand on 17.")

dealer = Dealer()
class Hand:

    def __init__(self):
        self.deck_value = {card: min(1 + self.rank.index(card[0]), 10)
                    for card in self.deck}
        self.hand_value = 0

    def value_hand(self):
        count_aces = 0
        for card in self.hand:
            if card[1] == 'A':
                count_aces += 1
                self.hand_value += self.deck_value[card[1]]
            if count_aces > 0 and self.hand_value < 12:
                self.hand_value += 10
                print("Hand value = {}.".format(self.hand_value))
                return self.hand_value

    def play_hand(self, dealer):
        dealer.value_hand()
        if dealer.value_hand <= 16:
            dealer.deal_hit()
        elif dealer.value_hand >= 17:
            print("Dealer stays.")
        else:
            if dealer.value_hand == 21:
                print("Dealer wins with 21!")
                dealer.clear_hand()


class Player:

    def play_hand(self, player):
        dealer = Dealer()
        player.value_hand()
        while player.value_hand < 21:
            hit_stay = input("Hit or stay? h/s").lower()
            if hit_stay == 'h':
                player.deal_hit()
            elif (player.value_hand > dealer.value_hand) or (dealer.value_hand > 21):
                print("You win!")
                dealer.clear_hand()

    def end_game(self):
        play_again = input("Do you want to play again? y/n").lower()
        deck = random.sample(cards, 52)
        if play_again == 'y':
            self.deck.shuffle()
            Dealer()
        else:
            print("Goodbye!")


blackjack_game()