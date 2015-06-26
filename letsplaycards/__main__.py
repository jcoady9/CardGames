
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

import argparse
import sys

from model.cardgame import CardGame
from games.solitaire import Solitaire

def main(argv = None):
	parser = argparse.ArgumentParser(description = "collection of card games")
	parser.add_argument("game", help = "name of the game you want to play")
	argv = parser.parse_args()

	game = CardGame()
	if argv.game == "solitaire":
		game = Solitaire()
	else:
		print "game is unavailable."
		sys.exit()

	game.update()

	while not(game.isGameOver()):
		while not(game.playUserMove(raw_input("make a move: "))):
			print "Invalid Move, try again."
		game.update()

		if game.hasComputerOpponent():
			print "opponent(s') move."
			for opponents in game.get_opponentsList():
				print "playing oppenent move"
			game.update()
	print "game over."

if __name__ == '__main__':
	main()
