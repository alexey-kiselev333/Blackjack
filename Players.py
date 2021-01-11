import abc

from Deck import Deck

class AbstractPlayer(abc.ABC):

    def __init__(self):
        self.cards=[]



    def ask_card(self):
        pass

class Player(AbstractPlayer):
    pass

class Dealler(AbstractPlayer):
    pass

class Bot(AbstractPlayer):

   def__init__(self):
    pass
