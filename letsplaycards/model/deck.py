
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

import random

from card import Card

class Deck:
	'represents the deck of 52 cards (excluding joker card)'

	suitsString = "DCSH" # Diamonds, Clubs, Spades, Hearts
	cardSymbols = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
	baseValues = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

	__cards = [] # list of cards represented by deck

	def __init__(self):
		"initialize the deck with 52 cards of 13 different values and 4 suites"

		self.__cards = [None] * 52

		for suit in Deck.suitsString:
			for k, symbol in Deck.cardSymbols:
				self.__cards[k] = Card(Deck.baseValues[k], symbol, suit)

	def drawCard(self):
		"draw a card from the top of the deck"
		return cards.top()

	def shuffle(self):
		"shuffles the order of the cards" 
		random.shuffle(self.__cards)
		