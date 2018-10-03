import hillClimbing

def runHillClimbing(filename='input.txt', steps=1000):

	piece_groups = hillClimbing.read_input(filename)
	initial_pieces = hillClimbing.initialize_board(piece_groups)

	print('\nInitial board state:\n')
	print(hillClimbing.draw_board(initial_pieces))
	print(*hillClimbing.count_all_attacks(initial_pieces))

	print('\nRunning hill climbing algorithm...\n')

	new_pieces = hillClimbing.hill_climbing(
	    initial_pieces
	)

	print('Resulting board state:\n')
	print(hillClimbing.draw_board(new_pieces))
	print(*hillClimbing.count_all_attacks(new_pieces))

if __name__ == '__main__':
    annealing_interface()