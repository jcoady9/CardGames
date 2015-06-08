
# Copyright (c) 2015 Joshua Coady

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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

print "\nsize of deck: " + str(len(cards))
print "top card: " + testDeck.drawCard().get_symbol()
print "size of deck: " + str(len(cards))
