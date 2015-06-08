
from deck import Deck

testDeck = Deck()

cards = testDeck.cards()

print "printing deck...\n"

i = 0
for suit in Deck.suitsString:
	string = []
	for symbol in Deck.cardSymbols:
		string.append(cards[i].get_symbol())
		i += 1
	print " ".join(string)

print "\ndeck after being shuffled...\n"

testDeck.shuffle()

cards = testDeck.cards()

i = 0
for suit in Deck.suitsString:
	string = []
	for symbol in Deck.cardSymbols:
		string.append(cards[i].get_symbol())
		i += 1
	print " ".join(string)

print "\n top card: " + testDeck.drawCard()
