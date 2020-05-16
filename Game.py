from BlackJack import *

"""
Author: BronTheDev
Simple Script Blackjack Game
"""


def Rules():
    print("The goal to BlackJack is to try and get to your hand equal to 21.\n"
          "You will get dealt a hand of 2 cards one facing down and one facing up.\n"
          "The value of you hand is the sum of your cards combined.\n"
          "The Valuation of cards: Ace = 11 or 1, Face cards(K,Q,J) = 10, Other cards = their number\n"
          "During the game you are able to Hit or Stand\n"
          "Hit means to Add another card to your deck, be wary because if the valuation of your deck goes over 21 you "
          "lose.\n"
          "Stand means to end your turn and round, do this when you feel like you don't want to add any more cards "
          "to your deck.\n")


def play(player):
    """ Simple method that allows user inputs to add cards towards their deck, show their hands or Stand and end
    their turn """
    while True:
        if player.stand() >= 21:
            break
        else:
            plays = input("Press Z to Hit, press X to Stand, Press C to Show Hand ")
            if plays == "z":
                player.hit_Me()
                player.show_Hand()
                continue
            if plays == "x":
                player.stand()
                break
            if plays == "c":
                player.show_Hand()
                continue


def begin_Game():
    """Simple method that initializes the game"""
    Rules()
    user = input("Are you ready to begin? Y or N: ")
    if user.capitalize() == "Y":
        Game()
    else:
        print("Ok, Bye Bye")


def Game():
    """Method that runs the game"""
    deck = Deck()
    deck.create_Deck()
    print("Creating User | Creating Dealer")
    user = input("What's your name? ")
    player = Player(deck, user)

    computer = Computer(deck)
    while player.pot > 0:
        current_Pot = player.bet() * 2
        currRound = True
        while currRound:
            print(f"The Current Pot is ${current_Pot}\n")
            deck.shuffle()
            print('Dealing Hands \n')
            computer.receive_Hand()
            computer.play_game()
            player.receive_Hand()
            player.show_Hand()
            play(player)
            compVal = computer.stand()
            playerVal = player.stand()
            print(f"\nDealers Hand: {computer.hand} | {player.name}'s Hand: {player.hand}\n")
            print(f"Dealer Has {computer.stand()} | {player.name} Has {player.stand()}")
            player.empty_Hand()
            computer.empty_Hand()

            if compVal > 21:
                print("The Dealer Busts. YOU WIN!")
                player.pot += current_Pot
                break
            elif playerVal > 21:
                print("You Bust. Dealer Wins.")
                break

            elif compVal <= 21 & playerVal <= 21:
                if compVal > playerVal:
                    print("Sorry you lost.")
                    break
                elif compVal == playerVal:
                    print("Draw")
                    continue
                else:
                    print(f"CONGRATS YOU WON {current_Pot}!!!")
                    player.pot += current_Pot
                    break

        if player.pot == 0:
            print(f"Sorry {player.name}, it seems as if you're out of money. Be sure to come back again. Bye Bye!")
            break
        else:
            continue_Game = input('Press Y if you would like to continue: ')
            if continue_Game == "y":
                continue
            else:
                if player.pot > 500:
                    print(
                        f"I guess you know when to call it a quits. Congratulations {player.name} on your winnings of "
                        f"{player.pot}")
                elif player.pot < 500:
                    print(f"Why are you leaving {player.name}? Don't you want to win back your money?. I guess not, "
                          f"you're leaving with only ${player.pot}")
                elif player.pot == 500:
                    print(f"Sorry to see you leave {player.name}. It Seems like you've broken even with ${player.pot}.")
                print("Bye")
                break


begin_Game()
