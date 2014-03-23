

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
						temp_moves = self.__valid_add_moves(player_num, move_type='step', old_x=i,old_y=j)
						moves.extend(temp_moves)
						self.board[i][j] = player_num

		return moves

	def __valid_add_moves(self, player_num, move_type='add', old_x=-1, old_y=-1):
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

					if self.is_valid(player_num,i,j):
						move = (player_num, move_type, old_x, old_y,  i, j)
						moves.append(move)

		return moves

	def is_valid(self, player_num, i, j):
		if self.board[i][j]!=0:
			return False
		else:
			self.board[i][j] = player_num
			for k in range(8):
				for l in range(8):	
					num_neighbors = self.num_surround(player_num, k, l)
					
					if num_neighbors>2:
						self.board[i][j] = 0
						return False

		self.board[i][j] = 0
		return True

	def num_surround(self, player_num, i, j):
		number = 0
		for k in range(i-1, i+2):
			if k<0 or k>7:
				continue
			
			for l in range(j-1, j+2):
				if l<0 or l>7:
					continue

				if self.board[k][l]==player_num:
					number += 1

		return number