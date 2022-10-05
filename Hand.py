
import Card

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Hand:    
    def __init__(self):
        self.cards = []
        self.value = 0  # current sum of the hand
        self.aces = 0   

    def add_card(self, card):
        # card passed in
        # from Deck.deal() --> it's a single card (suit & rank)
        self.cards.append(card)
        self.value += values[card.rank]   # this gets the value of the card and adds it to the hand value

        # track the aces:
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        # aces are initally valued at 11
        # if total value > 21 and we still have aces,
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1