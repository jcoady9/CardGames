
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

import sys

from model.cardgame import CardGame
from model.deck import Deck

class Solitaire(CardGame):
	'class representing a game of Solitaire'

	values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1]

	__stack = []
	__waste_pile = []
	__foundation_piles = []
	__tableau_piles = []

	def __init__(self):
		self.__stack = Deck(Solitaire.values)
		self.__stack.shuffle()
		self.__tableau_piles = [[] for __ in range(7)]
		self.__foundation_piles = [[] for __ in range(4)]

		for pile_size, pile in enumerate(self.__tableau_piles):
			i = 0
			while i <= pile_size:
				pile.append(self.__stack.drawCard())
				if i == pile_size:
					pile[i].set_visibility(True)
				i += 1

	def hasComputerOpponent(self):
		"returns false since solitaire is a single-player game"
		return False

	def drawCard(self):
		"draws a card from the top of the deck"
		if self.__waste_pile:
			self.__waste_pile.push(self.__stack.pop())
			return True
		return False

	def findCard(self, symbol):
		"find the card with the given symbol"
		waste_top = self.__waste_pile[-1]
		if self.__waste_pile:
			if waste_top.get_symbol() == symbol:
				return self.__waste_pile.pop()
		for pile in self.__tableau_piles:
			for i, card in enumerate(pile):
				if card.get_symbol() == symbol and card.isVisible():
					cards = pile[i:]
					del pile[i:]
					return cards
		return None

	def moveFoundation(self, card, foundation):
		"helper method to move a card to a Foundation pile"
		pile_num = int(foundation) - 1
		if pile_num < 0 or pile_num >= 4:
			return False
		if not self.__foundation_piles[pile_num]:
			if card.get_value() == 1:
				card = self.findCard(card.get_symbol())
				if card is not None:
					self.__foundation_piles[pile_num].append(card)
					return True
		if self.__foundation_piles[pile_num]:
			if card.get_suit() == self.__foundation_piles[pile_num][-1].get_suit() and card.get_value() == self.__foundation_piles[pile_num][-1].get_value() + 1:
				card = self.findCard(card.get_symbol())
				if isinstance(card, list):
					self.__foundation_piles[pile_num].extend(card)
				else:
					self.__foundation_piles[pile_num].append(card)
				return True
		return False

	def canMoveToTableau(self, card, tableau_pile):
		"ensures that the move to the tableau pile is valid"
		if len(tableau_pile) < 1:
			if card.get_value() == 13:
				return True
			return False
		if card.get_value() == tableau_pile[-1].get_value() - 1:
			red_suits = ["D", "H"]
			black_suits = ["C", "S"]
			if (card.get_suit() in black_suits) and (tableau_pile[-1].get_suit() not in  black_suits):
				return True
			if (card.get_suit() in red_suits) and (tableau_pile[-1].get_suit() not in red_suits):
				return True
		return False

	def moveTableau(self, card_symbol, tableau):
		"helper method to move a card (and any cards under it) to the Tableau pile"
		pile_num = int(tableau - 1)
		tableau_card = self.__tableau_piles[pile_num].top()
		for pile in self.__tableau_piles:
			for i, card in pile:
				if card.get_symbol() == card_symbol and self.canMoveToTableau(card, self.__tableau_piles[pile_num]):
					card = pile[i:]
					self.__tableau_piles[pile_num].extend(card)
					del pile[i:]
					return True
		return False

	def moveCard(self, args):
		"moves a card from one pile to another"
		args = str.partition(args, " ")
		if args[2][0] == "F":
			return self.moveFoundation(args[0], args[2])
		if args[2][0] == "T":
			return self.moveTableau(args[0], args[2])
		return False

	def flipCard(self, tableau):
		"flips a face down card to be face up"
		if self.__tableau_piles[int(tableau) - 1]:
			self.__tableau_piles[int(tableau) - 1].top().set_visibility(True)
		return

	def refillStack(self):
		"refills the stack pile with the waste pile once its depleted"
		if not self.__stack:
			self.__stack = self.__waste_pile.reverse()
			return True
		return False

	def playUserMove(self, args):
		"carries out player's move based on args"
		args = str.partition(args, " ")
		if args[0] == "quit":
			sys.exit()
		if args[0] == "move":
			return self.moveCard(args[2])
		if args[0] == "flip":
			self.flipCard(args[2])
		if args[0] == "draw" and args[2] == "card":
			return self.drawCard()
		if args[0] == "refill" and args[2] == "stack":
			self.refillStack()
		if args[0] == "help" or "rules":
			self.printRules()
		else:
			return False
		return True

	def update(self):
		"prints the game screen"

		stack_waste_str = []

		if self.__stack:
			stack_waste_str.append("X")
		else:
			stack_waste_str.append(" ")

		if self.__waste_pile:
			stack_waste_str.append(self.__waste_pile.top().get_symbol)
		else:
			stack_waste_str.append(" ")

		print stack_waste_str[0] + " " + stack_waste_str[1]

		foundation_strs = [None] * 4
		for i, foundation in self.__foundation_piles:
			for card in foundation:
				foundation_strs[i].append(card.get_symbol())
			print "F" + str(i + 1) + ": " + " ".join(foundation_strs[i])

		tableau_strs = [None] * 7
		for i, tableau in self.__tableau_piles:
			for card in tableau:
				if card.isVisible():
					tableau_strs[i].append(card.get_symbol())
				else:
					tableau_strs[i].append("X")
			print "T" + str(i + 1) + ": " + " ".join(tableau_strs[i])
		return

	def printRules(self):
		"print the rules of the game"
		#TODO: implement me
		return
