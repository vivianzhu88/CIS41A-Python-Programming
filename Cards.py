#Vivian Zhu
#Lab 7

import random

class Card :
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit]) 
    def __cmp__(self, other): # check the suits
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        # suits are the same... check ranks
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        # ranks are the same... it's a tie
        return 0 

class Deck(object) :
    def __init__(self):
        self.cards = []
        [[self.cards.append(Card(suit, rank)) for rank in range(1, 14)] for suit in range(4)]
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    def __len__(self):
        return len(self.cards)
    def pop_card(self):
        return self.cards.pop()
    def add_card(self, card):
        self.cards.append(card)
    def shuffle(self):
        random.shuffle(self.cards) 
    def move_cards(self, hand, num):
        [hand.add_card(self.pop_card()) for i in range(num)]

class Hand(object):
    def __init__(self, deck, numCards):
        self.deck = deck
        self.numCards = numCards
    def displayHand(self):
        print("THE HAND")
        print("________")
        [print(self.deck.pop_card()) for i in range (0, self.numCards)]
    def displayDeck(self):
        print("THE DECK")
        print("________")
        print(self.deck)
    
            
deck = Deck()
deck.shuffle()
hand = Hand(deck, 5)
hand.displayHand()
print()
hand.displayDeck()
