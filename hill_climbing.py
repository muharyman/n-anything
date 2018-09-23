from Catur import Anak_Catur
import a

# Algoritma Hill-Climbing
# Masukan : list_of_object Anak_Catur dan bilangan maksimum proses hill-climbing
def climbing(list_of_object, n):
    if n==0:
        return list_of_object
    else:
        # format best_solution : score, index, x, y
        best_solution = [a.scoreAkhir(list_of_object), -1, 0, 0]

        for i in range(0, len(list_of_object)):
            temp_list = list(list_of_object)
            x = temp_list.pop(i)

            # mengiterasi semua kemungkinan tetangga(satu anak catur dipindahkan)
            # mencari kemungkinan tetangga terbaik yang lebih baik dari list awal
            others = x.otherPositions(temp_list)
            for e in others:
                a_list = list(temp_list)
                a_list.append(e)
                other_score = a.scoreAkhir(a_list)

                # sebuah list_of_object dikatakan lebih baik jika score-nya lebih tinggi
                if other_score > best_solution[0]:
                    best_solution[0] = other_score
                    best_solution[1] = i
                    best_solution[2] = e.getX()
                    best_solution[3] = e.getY()

        # semua tetangganya lebih buruk sehingga langsung mengembalikan list
        if best_solution[1]==-1:
            return list_of_object

        # membentuk list terbaik dari proses hill climbing ke-n
        new_list = list(list_of_object)
        x = new_list.pop(best_solution[1])
        x.setCoor(best_solution[2], best_solution[3])
        new_list.append(x)

        return climbing(new_list, n-1)
