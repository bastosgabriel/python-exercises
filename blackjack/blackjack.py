'''
SIMPLE BLACKJACK TERMINAL GAME
'''

import random
import os
import platform

class Deck():
    
    def __init__(self):
        # deck.list is a list of tuples containing (card, suit, value)
        self.suit_list = ["diamonds","clubs","hearts","spades"]
        self.card_list = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        self.out_cards = []

    '''
    Returns a tuple with the number/face of the card and the suit (in this order)
    '''
    def buy(self):

        while True:
            card_num = self.card_list[random.randint(0,len(self.card_list)-1)]
            card_suit = self.suit_list[random.randint(0,len(self.suit_list)-1)]
            
            if ((card_num,card_suit) in self.out_cards):
                continue
            else:
                self.out_cards.append((card_num,card_suit))
                break
        return (card_num,card_suit)
        
class Player():

    def __init__(self):
        self.balance = 0
        self.cards = []
        self.open_cards = []

        for card,index in enumerate(self.cards):
            if (index == 1):
                continue
            self.open_cards.append(self.cards[card])

    def receive_card(self,*args):
        for index,card in enumerate(args):
            if (index == 1):
                self.cards.append(card)
                continue
            self.cards.append(card)
            self.open_cards.append(card)

class Table():

    def __init__(self):
        self.dealer_cards = []
        self.player_cards = []

    def clear(self):
        if platform.system() == 'Windows':
            os.system('cls')
        elif platform.system() == 'Linux' or platform.system() == 'Darwin':
            os.system('clear')

    def show(self,player_cards,dealer_cards):

        self.clear()

        # Print the game
        print("     ", end = '')
        for index,card in enumerate(dealer_cards):
            if index == 1:
                print("X   ", end = '')
            else:
                print(f"{card[0]}   ", end = '')
        
        print("")
        print(f"               ")
        print(f"               ")

        print("     ", end = '')
        for card in player_cards:
            print(f"{card[0]}   ", end = '')
        print("")

    def show_revealed(self,player_cards,dealer_cards):
        self.clear()

        # Print the game
        print("     ", end = '')
        for card in dealer_cards:
            print(f"{card[0]}   ", end = '')
        
        print("")
        print(f"               ")
        print(f"               ")

        print("     ", end = '')
        for card in player_cards:
            print(f"{card[0]}   ", end = '')
        print("")

    def menu(self):
        pass
    pass

class Game():

    def __init__(self):
        pass
    def sum_cards(self,card_list):

        card_value = {'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'10': 10,'J': 10,'Q': 10,'K': 10,'A': 11}
        sum_cards = 0

        for card in card_list:
            sum_cards += card_value[card[0]]

        if (sum_cards > 21) and ('A' in [card[0] for card in card_list]):
            sum_cards -= 10

        return sum_cards

gaming = "Y"

# Game loop
while gaming == "Y":
    player = Player()
    dealer = Player()
    deck = Deck()
    dealerWon = False

    # Give 2 cards to the player and dealer
    player.receive_card(deck.buy(),deck.buy())
    dealer.receive_card(deck.buy(),deck.buy())

    #print(player.cards)
    #print(dealer.cards)
    Table().show(player.cards,dealer.cards)

    # Player's turn
    while True:
        action = input("Hit or Stay? H/S ")
        if (action == "H"):
            # Receive another card
            player.receive_card(deck.buy())

            Table().show(player.cards,dealer.cards)

            if (Game().sum_cards(player.cards) > 21):
                print(f"Dealer wins!")
                dealerWon = True
                break
            continue

        elif (action == "S"):
            # Stop receiving cards
            break

    # Dealer's turn starts only if player didn't already loose
    if not(dealerWon):
        while True:
            if (dealer.cards[0][0] == 'A'):
                # Look for BlackJack
                Table().show_revealed(player.cards,dealer.cards)
                if (Game().sum_cards(dealer.cards) == 21):
                    print("Dealer wins!")
                    break

            dealer.receive_card(deck.buy())

            Table().show(player.cards,dealer.cards)

            if (Game().sum_cards(dealer.open_cards) > 17):
                # Reveal hidden card
                Table().show_revealed(player.cards,dealer.cards)

                if (Game().sum_cards(dealer.cards) > 21):
                    print(f"Player wins!")
                elif (Game().sum_cards(dealer.cards)) > (Game().sum_cards(player.cards)):
                    print(f"Dealer wins!")
                elif (Game().sum_cards(dealer.cards)) < (Game().sum_cards(player.cards)):
                    print(f"Player wins!")
                else:
                    print("The game tied!")
                break 
    gaming = input("Play again? Y/N ")

            






