

class Player(object):

	def __init__(self, color):

		self.color = color
		self.num_chips = 0
		self.board = [[0]*8 for i in range(8)]

	def choose_move(self):
		pass

	def force_move(self, move):
		(player_num, move_type, old_x, old_y, new_x, new_y) = move

		if move_type=='add':
			self.board[new_x][new_y] = player_num
		else:
			self.board[old_x][old_y] = 0
			self.board[new_x][new_y] = player_num

	def opponent_move(self, move):
		
		(player_num, move_type, old_x, old_y, new_x, new_y) = move

		if move_type=='add':
			self.board[new_x][new_y] = player_num
		else:
			self.board[old_x][old_y] = 0
			self.board[new_x][new_y] = player_num

	def valid_moves(self, player_num):
		moves = []

		if self.num_chips<10:
			#add moves
			move_type = 'add'

			moves = self.__valid_add_moves(player_num)
		else:
			pass
			#for each cell, clear it, then call add moves
			for i in range(8):
				for j in range(8):
					cell = self.board[i][j]

					if cell==player_num:
						self.board[i][j] = 0
						temp_moves = self.__valid_add_moves(player_num, move_type='step')
						moves.extend(temp_moves)

						self.board[i][j] = player_num

		print len(moves)

		return moves

	def __valid_add_moves(self, player_num, move_type='add'):
		moves = []

		for i in range(8):
			for j in range(8):
				#need to take into account goal zones
				if i==0 and j==0:
					continue

				if i==0 and j==7:
					continue

				if i==7 and j==0:
					continue

				if i==7 and j==7:
					continue

				chip = self.board[i][j]
				if chip==0:
					#check surrounding spaces for too many chips
					num_neighbor = self.num_surround(player_num, i, j)

					if num_neighbor<2:
						#then we have a valid move

						move = (player_num, move_type, -1, -1, i, j)

						moves.append(move)

		return moves


	def num_surround(self, player_num, i, j):

		max_num = -1
		for k in range(i-2, i+3):
			if k<0 or k>7:
				continue

			number = 0
			for l in range(j-2, j+3):
				if l<0 or l>7:
					continue

				if self.board[k][l]==player_num:
					number += 1

			max_num = max(max_num, number)

		return max_num