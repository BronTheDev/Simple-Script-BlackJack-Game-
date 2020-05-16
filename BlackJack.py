import random

'''
Complete BlackJack Card Game in Python.
Here are the requirements:

    You need to create a simple text-based BlackJack game
    The game needs to have one player versus an automated dealer.
    The player can stand or hit.
    The player must be able to pick their betting amount.
    You need to keep track of the player's total money.
    You need to alert the player of wins, losses, or busts, etc...

'''


class Card:
    def __init__(self, suit, label, value):
        self.suit = suit
        self.label = label
        self.value = value

    def __repr__(self):
        return f"{self.suit} {self.label}"

    def return_Val(self):
        return self.value


class Deck:

    def __init__(self):
        self.cards = []

    def create_Deck(self):
        """  Creates a Deck of Cards  """
        print('Creating Deck')
        for a in ["Heart", "Diamond", "Club", "Spade"]:
            for x in range(2, 11):
                self.cards.append(Card(a, x, x))
            self.cards.append(Card(a, "A", 11))
            self.cards.append(Card(a, "J", 10))
            self.cards.append(Card(a, "K", 10))
            self.cards.append(Card(a, "Q", 10))

    def shuffle(self):
        print('Shuffling Deck')
        random.shuffle(self.cards)

    def deal_Card(self):
        """:return: Provides the Player with a card and removes the cards from the deck  """

        return self.cards.pop()


class Player:
    def __init__(self, deck, name):
        self.hand = []
        self.pot = 500
        self.deck = deck
        self.name = name

    def bet(self):
        while True:
            try:
                print(f"\nYou have ${self.pot}")
                bet = int(input('How much would you like to bet? $'))
            except ValueError:
                print("Error invalid input please use a Whole Number.\n")
                continue
            if 0 < bet <= self.pot:
                self.pot -= bet
                print(f"You now have ${self.pot}")
                return bet
                break
            else:
                print(f"Your bet amount exceeds your funds of ${self.pot}. "
                      f"Please try again \n")
                continue

    def empty_Hand(self):
        self.hand = []

    def receive_Hand(self):
        for x in range(2):
            self.hand.append(self.deck.deal_Card())

    def show_Hand(self):
        print(f"Your hand: {self.hand} \n")

    def stand(self):
        total = 0
        for x in self.hand:
            total += x.return_Val()
        return total

    def hit_Me(self):
        """Adds card to Players deck"""
        self.hand.append(self.deck.deal_Card())


class Computer:
    def __init__(self, deck):
        self.hand = []
        self.pot = 200
        self.deck = deck

    def receive_Hand(self):
        for x in range(2):
            self.hand.append(self.deck.deal_Card())
        print(f"Dealers's hand: [{self.hand[0]}] and [?]")
        return self.hand

    def stand(self):
        total = 0
        for x in self.hand:
            total += x.return_Val()
        return total


    def empty_Hand(self):
        self.hand = []

    def play_game(self):
        """Computer AI that randomizes whether or not the computer hits or stands"""
        turn = True
        total = 0
        for x in self.hand:
            total += x.return_Val()
        while turn:
            if total < 19:
                if total < 14:
                    self.hand.append(self.deck.deal_Card())
                    continue
                elif 14 <= total <= 15:
                    chance = random.choice(["Hit", "Stand"])
                    if chance == "Hit":
                        self.hand.append(self.deck.deal_Card())
                        continue
                    else:
                        break
                elif 16 <= total <= 18:
                    chance = random.choice(["Hit", "Stand", "Stand","Stand","Stand"])
                    if chance == "Hit":
                        self.hand.append(self.deck.deal_Card())
                        continue
                    else:
                        break
            else:
                break
