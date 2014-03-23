from player import player, machine
from time import sleep
#0 for empty, 1 for white, 2 for black

class NetworkGame(object):

	def __init__(self,player1=True, player2=True):

		self.player1 = machine.RandomPlayer(WHITE)
		self.player2 = machine.RandomPlayer(BLACK)

		self.players = [0, self.player1, self.player2]

		self.board = [[0]*8 for i in range(8)]

	def run(self):
		#run game
		cur_player = 1
		next_player = 2
		while not self.is_over():
			#get move from player
			move = self.players[cur_player].choose_move()
			self.players[next_player].opponent_move(move)
			self.apply_move(move)

			#display move
			self.render()

			#change player move
			next_player = cur_player
			cur_player = (cur_player)%2 + 1

			sleep(.1)

		#declare winner or tie
		winner = None
		print winner
		return winner

	def is_over(self):
		return False


	def get_move(self,player):

		move = player.choose_move()

		return move

	def apply_move(self, move):
		#change the board by moving player_num
		(player_num, move_type, old_x, old_y, new_x, new_y) = move

		if move_type=='add':
			self.board[new_x][new_y] = player_num
		else:
			self.board[old_x][old_y] = 0
			self.board[new_x][new_y] = player_num

	def render(self):
		out_string = ''

		for i in range(8):
			for j in range(8):
				cell = self.board[i][j]

				out_string += str(cell)+' '

			out_string += '\n'

		print out_string


def main():
	global WHITE
	WHITE = 1
	global BLACK
	BLACK = 2
	
	#initialize board and players
	game = NetworkGame()

	game.run()

if __name__=="__main__":
	main()