import abc

from Deck import Deck

class AbstractPlayer(abc.ABC):

    def __init__(self,position):
        self.cards=[]
        self.position = position


    def ask_card(self):
        card = deck.get_card()
        self.cards.append(card)
        return True

class Player(AbstractPlayer):
    pass

class Dealler(AbstractPlayer):
    pass

class Bot(AbstractPlayer):

   def__init__(self):
    pass
