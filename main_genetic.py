from genetic import initPieces
from genetic import calcFitness
from genetic import sortGen
from genetic import genetic_process
from readFile import read_input
import board
import time
import random
import simulatedAnnealing

def runGenetic(filename='input.txt', steps=50, size=100, chance=0.3):
	gen = initPieces(size)
	print('\nRunning genetic algorithm...\n')
	print('Please wait, do not terminate...\n')
	sortbro = sortGen(gen,calcFitness(gen))
	genetic_process(sortbro[0],steps)

if __name__ == '__main__':
	runGenetic()