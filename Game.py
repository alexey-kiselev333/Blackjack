import Players
from Deck import Deck

from const import MESSAGES

import random


class Game:

    def __init__(self):
        self.players = []
        self.player = None
        # self.dealler = None
        self.all_players_count = 1
        self.deck = Deck()
        self.max_bet, self.min_bet =20,0

    @staticmethod
    def ask_starting(message):
        while True:
            choice = input(message)
            if choice == 'n':
                return False
            elif choice == 'y':
                return True

    def _launching(self):
        bots_count = int(input('Hello, write bots count '))
        self.all_players_count = bots_count + 1
        for i in range(bots_count):
            b = Players.Bot(position=i)
            self.players.append(b)
            print(b, ' is created')
        self.player = Players.Player(position=bots_count + 1)
        self.players.append(self.player)
    def ask_bet(self):
        for player in self.players:
            player.change_bet(self.max_bet, self.min_bet)
    def  first_descr(self):
        for player in self.players:
            player.ask_card(self.deck,2)
    def start_game(self):
        message = MESSAGES.get('ask_start')
        if not self.ask_starting(message=message):
            exit(1)
        #generating
        self._launching()
        self.ask_bet()
    def bet(self):

        self.bet()