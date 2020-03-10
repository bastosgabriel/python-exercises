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
        self.card_one = ()
        self.card_two = ()

class Table():

    def show(self):
        if platform.system() == 'Windows':
            clear = lambda: os.system('cls')
        elif platform.system() == 'Linux' or platform.system() == 'Darwin':
            clear = lambda: os.system('clear')

        clear()

        # Print the game


    def menu(self):
        pass
    pass




# Game loop
while True:
    player = Player()
    deck = Deck()

    player.card_one = deck.buy()
    player.card_two = deck.buy()

    while True:
        action = input("Hit or Stay? H/S")
        if (action == "H"):
            # receive another card


            pass
        elif (action == "S"):
            # stop receiving cards
            pass
        






