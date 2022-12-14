import random
import Card

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
               'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

class Deck:
    def __init__(self):
        self.entire_deck = []
        for suit in suits:
            for rank in ranks:
                self.entire_deck.append(Card.Card(suit, rank))

    def shuffle_deck(self):
        random.shuffle(self.entire_deck)

    def deal_one(self):
        return self.entire_deck.pop()

    def __str__(self):
        result = ''
        for card in self.entire_deck:
            result = result + '\n' + str(card)
        return "The deck has: "+ result

        
