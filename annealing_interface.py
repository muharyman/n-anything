import time

import simulatedAnnealing

def annealing_interface(filename='input.txt', steps=1000, temperature=1,
                        rate=10):
    piece_groups = simulatedAnnealing.read_input(filename)
    initial_pieces = simulatedAnnealing.initialize_board(piece_groups)

    print('\nInitial board state:\n')
    print(simulatedAnnealing.draw_board(initial_pieces))
    print(*simulatedAnnealing.count_all_attacks(initial_pieces))

    time.sleep(0.2)
    print('\nRunning simulated annealing algorithm...\n')

    new_pieces = simulatedAnnealing.simulated_annealing(
        initial_pieces, steps, temperature, rate
    )

    print('Resulting board state:\n')
    print(simulatedAnnealing.draw_board(new_pieces))
    print(*simulatedAnnealing.count_all_attacks(new_pieces))

if __name__ == '__main__':
    annealing_interface()