import random



bet = 0
money = 500
suit = ["Hearts", "Diamands", "Clubs", "Spades"]
Number = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Jack", "Queen", "King"]
Deck = []
hands = []



def genDeck(Deck):
	counter = 0
	for i in suit:
		for j in Number:
			Deck.append(j + " of " + i)

def round(Deck, money):
	bet = input("How much do you bet" + " You have " + str(money) + "?")
	money -= bet


genDeck(Deck)
round(Deck, money)
