import attackCount
from readFile import read_input
from board import initialize_board
from attackCount import count_all_attacks
from random import randint 
from board import draw_board

# Mengembalikan inisiasi awal sebanyak x gen

def initPieces(x) :
    gen = []
    for i in range(0, x) :
        piece_groups = read_input()
        pieces = initialize_board(piece_groups)
        gen.append(pieces)
    
    return gen

def calcFitness (gen) :
    fitnessVal = []
    for piece in gen :
        fitnessVal.append(count_all_attacks(piece))

    return fitnessVal

def sortGen (gen, fitnessVal) :
    newFitnessVal = []
    newGen = []
    tempFitnessVal = []
    tempGen = []
    j = len(fitnessVal)
    for idx in range(0,j) :
        idx_min = 0
        val_min = fitnessVal[0][0]
        for i in range(0, len(fitnessVal)) :
            if (val_min > fitnessVal[i][0]) :
                val_min = fitnessVal[i][0]
                idx_min = i
        tempFitnessVal.append(fitnessVal[idx_min])
        tempGen.append(gen[idx_min])
        gen.pop(idx_min)
        fitnessVal.pop(idx_min)
    
    for idx in range(0,j) :
        idx_max = 0
        valLeftMax = tempFitnessVal[0][0]
        val_max = tempFitnessVal[0][1]
        for i in range(0, len(tempFitnessVal)) :
            if (valLeftMax == tempFitnessVal[i][0]) :
                if (val_max < tempFitnessVal[i][1]) :
                    val_max = tempFitnessVal[i][1]
                    idx_max = i
            else :
                break
        newFitnessVal.append(tempFitnessVal[idx_max])
        newGen.append(tempGen[idx_max])
        tempGen.pop(idx_max)
        tempFitnessVal.pop(idx_max)
    
    new = newGen, newFitnessVal
    return new

def genetic_process (gen,x) :
    new_gen = []
    idx_max = int(len(gen)*9/10)
    for i in range (0,idx_max) :
        new_gen.append(gen[i])

    maxx = gen[0]
    for aa in range (0,x) :
        new_gens = []
       
        for temp_gen in gen :
            child1 = []
            child2 = []

            #Selection
            idx_border = randint(1,(len(temp_gen)-1))
            
            num_choose = randint(0,(len(new_gen)-1))

            for i in range (0,idx_border) :
                child1.append(temp_gen[i])
                child2.append(new_gen[num_choose][i])

            for i in range (idx_border,len(temp_gen)) :
                child1.append(new_gen[num_choose][i])
                child2.append(temp_gen[i])

            if (count_all_attacks(child1)[0] > count_all_attacks(child2)[0]) :
                new_gens.append(child2)
                temp = child2
            elif (count_all_attacks(child1)[0] < count_all_attacks(child2)[0]) :
                new_gens.append(child1)
                temp = child1
            else :
                if (count_all_attacks(child1)[1] < count_all_attacks(child2)[1]) :
                    new_gens.append(child2)
                    temp = child2
                else :
                    temp = child1
                    new_gens.append(child1)

            if (count_all_attacks(maxx)[0] > count_all_attacks(temp)[0]) :
                maxx = temp
            elif (count_all_attacks(maxx)[0] == count_all_attacks(temp)[0]) :
                if (count_all_attacks(maxx)[1] < count_all_attacks(temp)[1]) :
                    maxx = temp
                
            """
            #Mutation
            child1[randint(0,len(child1))] = randint(0,len(child1))
            idx_mut = randint(0,len(child1))
            """

        gen_temp = []
        for i in range(0,len(gen)) :
            gen_temp.append(new_gens[i])
        
        gen = sortGen(gen_temp, calcFitness(gen_temp))[0]

    print(draw_board(maxx))
    print(*count_all_attacks(maxx))