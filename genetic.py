import a

# Mengembalikan inisiasi awal sebanyak x gen
def initPieces(x) :
    gen = []
    for i in range(0, x) :
        gen.append(a.getList())
    
    return gen

def calcFitness (gen) :
    fitnessVal = []
    for val in gen :
        fitnessVal.append(a.totalConflict(val, "PUTIH"),a.totalConflict(val, "HITAM"))

    return fitnessVal

def sortGenLeft (gen, fitnessVal) :
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
        newFitnessVal = append(tempFitnessVal[idx_max])
        newGen.append(tempGen[idx_max])
        tempGen.pop(idx_max)
        tempFitnessVal.pop(idx_max)
    
    return newGen
