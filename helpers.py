from constants import VALUES, SUITS

def newDeck() -> list:
  deck = []
  for suit in SUITS:
    for value in VALUES:
      deck.append({'suit': suit, 'value': value, 'strength': VALUES[value]})
  return list(deck)