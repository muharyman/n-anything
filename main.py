from genetic import initPieces
from genetic import calcFitness
from genetic import sortGen
from genetic import genetic_process
import board

gen = initPieces(100)
print(gen[0])
fitness = calcFitness(gen)
sortbro = sortGen(gen,fitness)
genetic_process(sortbro[0],100)