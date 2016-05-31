class Hand(Dealer): #dealer

    def __init__(self):
        super().__init__()  # inheriting all from dealer
        self.deck_value = {card: min(1 + self.rank.index(card[0]), 10)
                    for card in self.deck}
        self.hand_value = 0  #dealer_value??
        self.hit
        self.stay = print("I'll stay.")
        self.hit_stay = input("Hit or stay? h/s").lower()

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
            dealer.stay
        elif (player.value_hand > dealer.value_hand) or (dealer.value_hand > 21):
            print("You win!")
            dealer.clear_hand()
            end_game()
        else:
            if dealer.value_hand == 21:
                print("Computer wins!")
                dealer.clear_hand()
                end_game()

    def end_game(self):
        play_again = input("Do you want to play again? y/n").lower()
        if play_again == 'y':
            dealer.shuffle_deck
            deal_hand()
        else:
            print("Goodbye!")

 Hand()
