from Players import Bot

from Deck import Deck

from const import MESSAGES

import random


class Game:

    def __init__(self):
        self.players = []
        self.player = None
        self.dealler = None
        self.all_players_count = 1
        self.deck = Deck()
        

    @staticmethod
    def ask_starting(message):
        while True:
            choice = input(message)
            if choice == 'n':
                return False
            elif choice == 'y':
                return True

    def start_game(self):
        message = MESSAGES.get('ask_start')
        if not self.ask_starting(message=message):
            exit(1)

        bots_count = input('Hello, write bots count')
        self.all_players_count = bots_count + 1
        for _ in range(bots_count):
            b = Bot(position=random.randint(0, self.all_players_count))
            self.players.append(b)
