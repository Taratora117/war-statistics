from ast import Param
import random
from helpers import newDeck

class Game:
  def __init__(self):
    self.gameHistory = []
    self.deck = newDeck()
  
  def reset(self):
    self.gameHistory = []
    self.deck = newDeck()

  def record(self, human, ai):
    self.gameHistory.append({"human": len(human), "ai": len(ai)})

  def play(self) -> list:
    # init
    deck = self.deck
    random.shuffle(deck)

    humanDeck = deck[0:26]
    aiDeck = deck[26:52]
    
    cards = {"human": None, "ai": None, "pot": []}
    
    # loop
    war = False
    while ((len(humanDeck) > 0 and len(aiDeck) > 0) or war):
      
      # if cards run out during war
      if len(humanDeck) == 0:
        humanDeck.append(aiDeck.pop(0))
      elif len(aiDeck) == 0:
        aiDeck.append(humanDeck.pop(0))
      
      # draw card
      cards["human"] = humanDeck.pop(0)
      cards["ai"] = aiDeck.pop(0)

      # add cards to pot
      cards["pot"].extend([cards["human"], cards["ai"]])

      # draw more cards for war
      if war and (len(cards["pot"]) == 2 or (len(cards["pot"]) - 2) % 6 != 0):
        continue

      # evaluate cards
      if cards["human"]["strength"] > cards["ai"]["strength"]:
        war = False
        random.shuffle(cards["pot"])
        humanDeck.extend(cards["pot"])
      elif cards["human"]["strength"] < cards["ai"]["strength"]:
        war = False
        random.shuffle(cards["pot"])
        aiDeck.extend(cards["pot"])
      else:
        war = True
        continue


      # reset
      cards["human"] = None
      cards["ai"] = None
      cards["pot"] = []

    return len(humanDeck) == 0
