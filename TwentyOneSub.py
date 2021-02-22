import random

CHEAT_MODE = False
DEALER_STOPS_AT = 15

# -----------------------------------------------------------------------------
class Card:
    suit_str = ("Spades", "Hearts", "Diamonds", "Clover")
    index_str = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King")


    def __init__(self, suit, index):
        self.suit = suit
        self.index = index             # index is 0 to 12
        self.value = index + 1         # value is 1 to 13


    def to_str(self):
        s = self.index_str[self.index] + " of " + self.suit_str[self.suit]
        s += "     "   # Make string for all cards 18 characters long with trailing spaces
        return s[:18]

# -----------------------------------------------------------------------------
class DeckOfCards:
    card = Card(0,0)
    cards = [card] * 52               # This line could be removed, if it is declared in __init__. But I think this is the right place


    def __init__(self):
        # self.card = Card(0, 0)      # This variable could be inittiate here or further above. Or in both places
        self.cards = [self.card] * 52 # This line must be here if an instance of DeckofCards should be created more than once. Seems to apply for lists only.
        self.cardsLeft = 52

        for s in range (4):
            for v in range(13):
                i = s * 13 + v
                self.cards[i] = Card(s, v)


    def shuffleDeck(self):
        random.shuffle(self.cards)


    def requestNewCard(self):
        self.cardsLeft -= 1
        x =  self.cards.pop()
        if CHEAT_MODE:
            x.value = int(input("CHEAT_MODE, enter value of card: "))
        return x


    def printout(self):
        for i in range (52):
            if i % 13 == 0: print()
            print(i, self.cards[i].to_str()+ ", ", end = "")
        print()


# -----------------------------------------------------------------------------
class Player:
    # totalScore = 0

    def __init__(self):
        self.totalScore = 0
        self.aceCounter = 0


    def calcTotalScore(self, points):
        if points == 1:
            points = 14
            self.aceCounter += 1

        self.totalScore += points
        if self.totalScore > 21 and self.aceCounter > 0:
            self.totalScore -= 13
            self.aceCounter -= 1


