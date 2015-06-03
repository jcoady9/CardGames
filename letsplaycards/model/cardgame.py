
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

class CardGame:
	'base class for card game classes'

	__deck = Deck() #the deck of cards for the game

	__gameOver = False #boolean to determine if game is over
	__opponents = [] # list of computer opponents if the game requires more than one player

	def __init__(self, hasOpponents = False, opponents_list = None):
		if hasOpponents:
			self.__opponents = opponents_list

	def validMoveExists(self):
		"determines whether there are any more possible moves for the human player"
		return self.__gameOver

	def isGameOver(self):
		"determines if the game is over"
		return self.__gameOver

	def hasComputerOpponent(self):
		"determines if there are any computer opponents"
		return True

	def get_opponentsList(self):
		return self.__opponents

	def playComputerMove(self, opponent):
		"plays the move of the computer opponent"
		print "playing computer oppnent's move."
		return

	def playUserMove(self, args):
		"takes the user input and parses args into usable data"
		if args == "done":
			self.__gameOver = True
			return True
		print args
		return False

	def update(self):
		"update the game screen (currently just the terminal dispaly)"
		print "updating...."
		return

	def printRules(self):
		"displays the rules of the game"
		return ""
