
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

import getopt

from model.cardgame import CardGame

def main(argv = None):
	print "Hello card game fans!"

	game = CardGame(True, [" ", "!", "#"])

	while not(game.isGameOver()):

		print "your move."

		while not(game.playUserMove(raw_input("make a move: "))):
			print "Invalid Move, try again."

		game.update()

		print "opponent(s') move."

		if game.hasComputerOpponent():
			for opponents in game.get_opponentsList():
				print "playing oppenent move"

		game.update()
		
	print "game over."


if __name__ == '__main__':
	main()
