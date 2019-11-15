import random



bet = 0
money = 500
suit = ["Hearts", "Diamands", "Clubs", "Spades"]
Number = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Jack", "Queen", "King"]
Deck = []
def genHand():
	counter = 0
	for i in suit:
		for j in Number:
			Deck.append(j + " of " + i)
			
	return Deck

print(genHand())