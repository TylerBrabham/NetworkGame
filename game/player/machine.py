from player import Player
from random import randint

class MachinePlayer(Player):
	def __init__(self, color):
		self.color = color

		#call super

	def choose_move(self):
		moves = self.valid_moves()

		return moves[0]

class RandomPlayer(Player):
	
	
	def __init__(self, color):
		self.color = color
		self.num_chips = 0
		self.board = [[0]*8 for i in range(8)]

		#call super
		

	def choose_move(self):
		moves = self.valid_moves(self.color)

		n = len(moves)
		move = moves[randint(0,n-1)]
		self.force_move(move)

		self.num_chips = min(10, self.num_chips+1)

		return move
