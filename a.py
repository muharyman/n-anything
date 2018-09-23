# Fungsi - fungsi tambahan
from Catur import Anak_Catur
import random


# Mengambil informasi dari "file.txt"
# Mengembalikan list_of_object Anak_Catur dalam posisi random
def getList():
	f = open('input.txt','r')
	list_of_object = []
	for line in f :
		info = line.split()
		for i in range(0 , int(info[2])):
			char = info[1][0]
			if info[0][0]=='B':
				char = char.lower()

			# menambahkan objek Anak_Catur ke dalam list dengan posisi unik
			objek = Anak_Catur(char , random.randint(0,7),random.randint(0,7))
			while objek.isSameCoorExist(list_of_object) :
				objek = Anak_Catur(char , random.randint(0,7),random.randint(0,7))

			list_of_object.append(objek)
	return list_of_object

# Mengembalikan jumlah total konflik catur-catur berwarna PUTIH dengan catur lain
# berdasarkan warna yang ingin dihitung konfliknya ("PUTIH" atau "HITAM")
def totalConflict(list_of_object, color):
	total = 0
	for e in list_of_object:
		if e.isWhite():
			total += e.conflict(list_of_object, color)
	return total

# Total nilai secara keseluruhan
def scoreAkhir(list_of_object):
	return (totalConflict(list_of_object, "HITAM") - totalConflict(list_of_object, "PUTIH"))

# Mengembalikan character dari objek Anak_Catur yang memiliki kordinat
# jika tidak ada maka mengembalikan '*'
def charCoor(list_of_object, x, y):
	for e in list_of_object :
		if e.getX() == x and e.getY() == y :
			return e.getChar()
	return '*'

def printHasil(list_of_object):
	for i in range (0 , 8):
		for j in range (0 , 8):
			print(charCoor(list_of_object, i , j), end=" ")
		print ('\n')
