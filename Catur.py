import random

class Anak_Catur :
	# constructor objek Anak_Catur
	def __init__(self, char, x, y):
		self.char = char
		self.x = x
		self.y = y

	# setter and getter
	def setX(self, x):
		self.x = x
	def setY(self, y):
		self.y = y
	def setCoor(self, x, y):
		self.setX(x)
		self.setY(y)
	def getChar(self):
		return self.char
	def getX(self):
		return self.x
	def getY(self):
		return self.y

	
	# Memeriksa apakah ada objek dalam list_of_object yang memiliki posisi sama
	def isSameCoorExist(self, list_of_object):
		for e in list_of_object:
			if e.x == self.x and e.y == self.y :
				return True
		return False 

	# Mengembalikan list of object yang memenuhi kriteria "otherPositions"
	# "otherPositions" adalah semua kemungkinan objek dengan posisi lain yang tidak sama dengan semua objek pada list_of_object
	def otherPositions(self, list_of_object):
		others = []
		for j in range(0,8):
			for i in range(0,8):
				obj = Anak_Catur(self.char, i, j)
				if not(obj.isSameCoorExist(list_of_object)) and not(obj.getX()==self.x and obj.getY()==self.y):
					others.append(obj)
		return others
	
	# Mengecek apakah Anak_Catur berwana putih atau tidak
	def isWhite(self):
		return (self.char>='A' and self.char <= 'Z')

	# Menghitung jumlah konflik Anak_Catur dengan Anak_Catur lain berdasarkan warna putih/hitam
	def conflict(self, list_of_object, color):
		if color=="PUTIH":
			min = 'A'
			max = 'Z'
		else:
			min = 'a'
			max = 'z'

		N = 0
		# Menghitung jumlah konflik jika Anak_Catur adalah knight (kuda)
		if self.char=='K' or self.char=='k':
			for e in list_of_object:
				if e.char >= min and e.char <= max:
					if e.x==self.x-1 and e.y==self.y-2:
						N +=1
					elif e.x==self.x-2 and e.y==self.y-1:
						N +=1
					elif e.x==self.x-2 and e.y==self.y+1:
						N +=1
					elif e.x==self.x-1 and e.y==self.y+2:
						N +=1
					elif e.x==self.x+2 and e.y==self.y+1:
						N +=1
					elif e.x==self.x+1 and e.y==self.y+2:
						N +=1
					elif e.x==self.x+1 and e.y==self.y-2:
						N +=1
					elif e.x==self.x+2 and e.y==self.y-1:
						N +=1
		else:
			# Menghitung jumlah konflik jika Anak_Catur adalah rock (benteng) atau queen(ratu)
			if self.char=='R' or self.char=='r' or self.char=='Q' or self.char=='q':
				# list of info Anak_Catur lain yang konflik dengan Anak_Catur tsb. (atas, bawah, kiri, kanan)
				chars_conflict = [[' ', 0, 0], [' ', 0, 0], [' ', 0, 0], [' ', 0, 0]]

				for e in list_of_object:
					# kondisi konflik di atas Anak_Catur
					if e.x==self.x and e.y<self.y:
						if chars_conflict[0][0]==' ' or chars_conflict[0][2] < e.y:
							chars_conflict[0][0] = e.char
							chars_conflict[0][1] = e.x
							chars_conflict[0][2] = e.y

					# kondisi konflik di bawah Anak_Catur
					elif e.x==self.x and e.y>self.y:
						if chars_conflict[1][0]==' ' or chars_conflict[0][2] > e.y:
							chars_conflict[1][0] = e.char
							chars_conflict[1][1] = e.x
							chars_conflict[1][2] = e.y

					# kondisi konflik di kiri Anak_Catur
					elif e.x<self.x and e.y==self.y:
						if chars_conflict[2][0]==' ' or chars_conflict[0][1] < e.x:
							chars_conflict[2][0] = e.char
							chars_conflict[2][1] = e.x
							chars_conflict[2][2] = e.y

					# kondisi konflik di kanan Anak_Catur
					elif e.x>self.x and e.y==self.y:
						if chars_conflict[3][0]==' ' or chars_conflict[0][1] > e.x:
							chars_conflict[3][0] = e.char
							chars_conflict[3][1] = e.x
							chars_conflict[3][2] = e.y
						
				temp = [1 for e in chars_conflict if e[0] >= min and e[0] <= max]
				N += sum(temp)

			# Menghitung jumlah konflik jika Anak_Catur adalah bishop (gajah) atau queen(ratu)
			if self.char=='B' or self.char=='b' or self.char=='Q' or self.char=='q':
				# list of info Anak_Catur lain yang konflik dengan Anak_Catur tsb. (atas-kiri, atas-kanan, bawah-kiri, bawah-kanan)
				chars_conflict2 = [[' ', 0, 0], [' ', 0, 0], [' ', 0, 0], [' ', 0, 0]]

				for e in list_of_object:
					# nilai gradient harus 1 atau -1 (menyatakan posisi Anak_Catur diagonal)
					if self.x - e.x == 0:
						m = 0
					else:
						m = (self.y - e.y)/(self.x - e.x)

					if int(m)==1 or int(m)==-1:
						# kondisi konflik di atas-kiri Anak_Catur
						if e.y<self.y and e.x<self.x:
							if chars_conflict2[0][0]==' ' or chars_conflict2[0][2] < e.y:
								chars_conflict2[0][0] = e.char
								chars_conflict2[0][1] = e.x
								chars_conflict2[0][2] = e.y

						# kondisi konflik di atas-kanan Anak_Catur
						elif e.y<self.y and e.x>self.x:
							if chars_conflict2[1][0]==' ' or chars_conflict2[0][2] < e.y:
								chars_conflict2[1][0] = e.char
								chars_conflict2[1][1] = e.x
								chars_conflict2[1][2] = e.y

						# kondisi konflik di bawah-kiri Anak_Catur
						elif e.y>self.y and e.x<self.x:
							if chars_conflict2[2][0]==' ' or chars_conflict2[0][2] > e.y:
								chars_conflict2[2][0] = e.char
								chars_conflict2[2][1] = e.x
								chars_conflict2[2][2] = e.y

						# kondisi konflik di bawah-kanan Anak_Catur
						elif e.y>self.y and e.x>self.x:
							if chars_conflict2[3][0]==' ' or chars_conflict2[0][2] > e.y:
								chars_conflict2[3][0] = e.char
								chars_conflict2[3][1] = e.x
								chars_conflict2[3][2] = e.y

				temp = [1 for e in chars_conflict2 if e[0] >= min and e[0] <= max]
				N += sum(temp)

		# Mengembalikan jumlah konflik
		return N

	


