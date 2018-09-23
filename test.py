from hill_climbing import climbing
import a
from Catur import Anak_Catur

#Test
soal = a.getList()
a.printHasil(soal)
print (a.totalConflict(soal, "PUTIH"))
print (a.totalConflict(soal, "HITAM"))
print('\n')
answer = climbing(soal, 20)
a.printHasil(answer)
print (a.totalConflict(answer, "PUTIH"))
print (a.totalConflict(answer, "HITAM"))