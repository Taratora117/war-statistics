from helpers import newDeck

class Game:
  def __init__(self):
    self.gameHistory = []
    self.deck = newDeck()
  
  def reset(self):
    self.gameHistory = []
    self.deck = newDeck()

  def record(self, data):
    self.gameHistory.append(data)

  def play(self) -> list:
    # implement game loop
    
    return self.gameHistory

