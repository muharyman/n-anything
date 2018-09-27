import time

import annealing

def annealing_easy(filename):
    piece_groups = annealing.read_input(filename)
    initial_pieces = annealing.initialize_board(piece_groups)

    print('Initial board state:\n')
    print(annealing.draw_board(initial_pieces))
    print(*annealing.count_all_attacks(initial_pieces))

    time.sleep(1)
    print('\nRunning simulated annealing algorithm...\n')

    new_pieces = annealing.simulated_annealing(initial_pieces)

    print('Resulting board state:\n')
    print(annealing.draw_board(new_pieces))
    print(*annealing.count_all_attacks(new_pieces))

annealing_easy('input.txt')