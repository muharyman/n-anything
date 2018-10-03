from genetic import initPieces
from genetic import calcFitness
from genetic import sortGen
from genetic import genetic_process
from readFile import read_input
import board
import time
import random
import simulatedAnnealing

# gen = initPieces(100)
# print(gen[0])
# fitness = calcFitness(gen)
# sortbro = sortGen(gen,fitness)
# genetic_process(sortbro[0],100)

filename='input.txt'

# SIMULATED ANNEALING
piece_groups = simulatedAnnealing.read_input(filename)
initial_pieces = simulatedAnnealing.initialize_board(piece_groups)

print('\nInitial board state:\n')
print(simulatedAnnealing.draw_board(initial_pieces))
print(*simulatedAnnealing.count_all_attacks(initial_pieces))

time.sleep(0.2)
print('\nRunning simulated annealing algorithm...\n')

new_pieces = simulatedAnnealing.simulated_annealing(initial_pieces)

print('Resulting board state:\n')
print(simulatedAnnealing.draw_board(new_pieces))
print(*simulatedAnnealing.count_all_attacks(new_pieces))