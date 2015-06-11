
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

from solitaire import Solitaire
from model.card import Card

testSolitaire = Solitaire()

#test hasComputerOpponent()
assert testSolitaire.hasComputerOpponent() is False

#test moveFoundation()
cards = []
cards.append(Card(3, "3H", "H"))
cards.append(Card(4, "4H", "H"))
cards.append(Card(2, "2H", "H"))
cards.append(Card(2, "2D", "D"))
cards.append(Card(1, "AH", "H"))
cards.append(Card(10, "JH", "H"))

testSolitaire._Solitaire__waste_pile = cards

for card in testSolitaire._Solitaire__waste_pile:
	print card.get_symbol()

assert testSolitaire.moveFoundation(cards.pop(), 1) is False # JH on empty
assert testSolitaire.moveFoundation(cards.pop(), 1) is True  # AH on empty
assert testSolitaire.moveFoundation(cards.pop(), 1) is False # 2D on AH
assert testSolitaire.moveFoundation(cards.pop(), 1) is True  # 2H on AH
assert testSolitaire.moveFoundation(cards.pop(), 1) is False # 4H on 2H
assert testSolitaire.moveFoundation(cards.pop(), 1) is True  # 3H on 2H


 
