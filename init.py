import random



bet = 0
money = 500
suit = ["Hearts", "Diamands", "Clubs", "Spades"]
Number = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Jack", "Queen", "King"]
Deck = []
hands = []
def genHand(hands):
	counter = 0
	for i in suit:
		for j in Number:
			Deck.append(j + " of " + i)
	print("How many people do you want to play with?")
	players = input()
	print(players)

genHand(hands)