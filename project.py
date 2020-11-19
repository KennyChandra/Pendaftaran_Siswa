from os import system

def tampilan_menu():
	system("cls")
	system("title Pendaftaran Murid Baru")
	system("color b")
	tampilan_awal = """
	_________________________________
	|  PENDAFTARAN MURID BARU SMA 1 |       SSSSSSSS   M           M   AAAAAAAA       11111
	|===============================|      S           M M       M M  A        A     11  11
	|[A]. Formulir Pendaftaran      |     S            M   M   M   M A          A    1   11
	|[B]. Lihat Informasi Murid     |      SS          M     M     M A          A        11
	|[C]. Cari Informasi Murid      |        SSSSS     M           M A AAAAAAAA A        11
	|[D]. Informasi Sekolah         |             SS   M           M A          A        11
	|[E]. Informasi Khusus Admin    |               S  M           M A          A        11
	|[F]. Keluar                    |      SSSSSSSSS   M           M A          A    111111111
	=================================
	"""
	print(tampilan_awal)

def option_a():
	system("cls")
	print("Mendaftarkan Murid\n            -Informasi Murid-")
	print("Note: Sebelum mengisi data mohon baca peraturan yang dapat dilihat di opsi D[4].")
	nama = input("Nama Lengkap:\t").capitalize()
	tanggal = input("Masukkan tanggal lahir:\t")
	tempat = input("Tempat lahir:\t")
	nam = input("Nama ayah:\t").capitalize()
	nama2 = input("Nama ibu:\t").capitalize()
	kerja = input("Pekerjaan ayah:\t")
	kerja2 = input("Pekerjaan ibu:\t")
	telp = input("No telpon orangtua/ anak:\t")
	alamat = input("Alamat rumah:\t")
	asal = input("Asal sekolah:\t").capitalize()
	agama = input("Agama:\t").capitalize()
	riwayat = input("Apakah pernah terjerat dalam masalah di sekolah lama, jika iya tuliskan:\t")
	atur = input("Apakah setuju dengen peraturna sekolah yang telah ditetapkan :")
	respond = input(f"Yakin ingin menyimpan. Tekan 'S' untuk simpan : ")
	if respond.upper() == "S":
		students[nama] = {
			"Tg" : tanggal,
			"Tl" : tempat,
			"Na" : nam,
			"Ni" : nama2,
			"Ka" : kerja,
			"Ki" : kerja2,
			"Te" : telp,
			"Al" : alamat,
			"As" : asal,
			"Ag" : agama, 
			"Ri" : riwayat,
			"Se" : atur,
		}
		print("Data tersimpan.")
	else:
		print("INVALID Respond")
	input("Press ENTER to return.")

def option_b():
	system("cls")
	print("Daftar Murid yang Telah Disimpan\n        -  DAFTAR MURID -")
	if len(students) == 0:
		print("Belum ada data yang tersimpan saat ini.")
	else:
		for student in students:
			print("Nama:\t", student)
			print("Asal Sekolah\t:", students[student]["As"])
			print()
	input("Press ENTER to return to MENU.")					

def option_cs(student):
	if student in students:
		print("    - HASIL PENCARIAN -")
		print("Nama:\t", student)
		print("Asal Sekolah:\t", students[student]["As"])
		print("Masukkan Code untuk informasi selanjutnya")
		Password = input("Code : ")
		if Password == "24353":
			print("Nama:\t", student)
			print("Tanggal Lahir:\t", students[student]["Tg"])
			print("Tempat Lahir:\t", students[student]["Tl"])
			print("Nama ayah:\t", students[student]["Na"])
			print("Nama ibu:\t", students[student]["Ni"])
			print("Pekerjaan ayah:\t", students[student]["Ka"])
			print("Pekerjaan ibu:\t", students[student]["Ki"])	
			print("Telepon:\t", students[student]["Te"])
			print("Alamat:\t", students[student]["Al"])
			print("Asal Sekolah:\t", students[student]["As"])
			print("Agama:\t", students[student]["Ag"])
			print("Riwayat:\t", students[student]["Ri"])
			print("Persetujuan akan peraturan sekolah:\t", students[student]["Se"])
			print()
			return True
		else:
			system("cls")
	else:
		print("Data tidak ditemukan.")
		return False

def option_c():
	system("cls")
	print("- PENCARIAN INFORMASI MURID -")
	nama = input("Nama Murid yang dicari : ").capitalize()
	option_cs(nama)
	input("Press ENTER to return to MENU")

def d_tampilan():
	system("cls")
	system("title Informasi Sekolah SMA 1")
	system("color a")
	info = """
	|****************************************|
	|     -INFORMASI TENTANG SEKOLAH-        |
	|****************************************|
	|[1]                                     |
	|=>Yayasan                               |
	|[2]                                     |
	|=>Kepala and Wakil kepala sekolah       |
	|[3]                                     |
	|=>Nama nama guru dan mapel yang diajar  |
	|[4]                                     |
	|=>Peraturan peraturan Sekolah           |
	|[5]                                     |
	|=>Keluar                                |
	|                                        |  
	==========================================
	"""
	print(info)

def option1():
	yayasan = """
	>YAYASAN SEKOLAH SMA 1<
	-----------------------
	 Yayasan BUDI SUTOEMO
	"""
	print(yayasan)

def option2():
	op2 = """
	Nama Kepala Sekolah : Sutardjo Supratman S.Pd (12 Tahun)
	________________________________________________________

	Nama Wakil Kepala Sekolah : Budi Sutarman S.Pd (8 Tahun)
	
	"""
	print(op2)

def option3():
	system("cls")
	guru_pelajaran = """
	_________________________________________________________________
	|         Nama Guru         |            Mata Pelajaran         |
	|================================================================
	|[1].Sutardjo Supratman     |	Biologi SMA                     |
	|[2].Budi Sutarman          |	Bahasa Indonesia SMA XI         |
	|[3].Anton Aki              |	Pendidikan Kewarganegaraan SMA  |
	|[4].Wati Bunga             |	Seni Budaya                     |	
	|[5].Yanto Intan            |	Fisika SMA XII                  |
	|[6].Ekko Prajoyo           |	Ekonomi SMA XII, XI             |
	|[7].Andi Dy                |	Kimia SMA XI, XII               |	
	|[8].Steven Gunardo         |	Bahasa Inggris                  |
	|[9].Amir Soleh             |	Ekonomi SMA X, Akuntansi SMA XI |
	|[10].Ahmat Suyono          |	Akuntansi SMA X, XII            |
	|[11].Dimas Kanjeng         |	Fisika SMA X, XI                |
	|[12].Rama Yani             |	Kimia SMA X                     |
	|[13].Genta Dirga           |	Bahasa Indonesia SMA X, XII     |
	|================================================================

	"""
	print(guru_pelajaran)

def option4():
	system("cls")
	peraturan = """
												- PERATURAN SEKOLAH SMA 1 -

	1. Pelajaran akan dimulai setiap jam 07.30 setiap harinya kecuali hari Senin (upacara bendera).
	2. Siswa harus berada di dalam kelas paling lambat 10 menit sebelum jam pelajaran dimulai.
	3. Bagi siswa yang datang terlambat maka diwajibkan untuk melapor ke guru piket dan membawa surat izin masuk kelas dari guru piket.
	4. Siswa yang 3 kali datang terlambat secara berturut turut, akan dikenai sanksi berupa surat peringatan 1.
	5. Siswa tidak diperkenankan keluar masuk ruang kelas tanpa seizin dari guru yang sedang mengajar.
	6. Siswa harus berseragam lengkap sesuai ketentuan yang berlaku:
		a. Senin – Selasa : seragam putih abu-abu.
		b. Rabu – Kamis  : seragam batik sekolah.
		c. Jumat – Sabtu : seragam Pramuka.
		d. Siswi diwajibkan untuk memakai bawahan rok dan baju lengan panjang.
	7. Seluruh siswa diwajibkan untuk berpakaian rapi dan sesuai dengan ketentuan baik di sekolah maupun diluar sekolah.
	8. Bagi siswa yang berhalangan hadir, diharapkan untuk membuat surat keterangan yang ditandatangani oleh orang tua siswa atau wali.
	9. Surat keterangan tanpa tanda tangan orang tua atau wali dianggap tidak sah.
	10. Siswa yang tidak hadir di kelas tanpa surat keterangan yang sah dianggap alpa pada hari tersebut..
	11. Siswa yang tiga kali berturut-turut hadir tanpa keterangan maka orang tua siswa akan dipanggil untuk menghadap wali kelas.
	12. Siswa yang dengan jumlah alpa lebih dari 20 kali dalam satu tahun atau 2 semester, maka dinyatakan tidak naik kelas. tanpa pengecualian.
	13. Siswa harus menjaga kebersihan lingkungan sekolah dan dilarang membuang sampah sembarangan.
	14. Setiap siswa diwajibkan untuk mengikuti kegiatan-kegiatan yang dilakukan oleh pihak sekolah seperti senam, kegiatan Jum’at bersih dll.
	15. Siswa harus bertingkah laku sopan dan baik terhadap guru, siswa ataupun perangkat sekolah lainnya.
	16. Siswa dilarang berambut gondrong atau panjang (bagi laki laki), membawa senjata tajam, narkoba, rokok ataupun obat obatan berbahaya lainnya.
	17. Siswa dilarang merokok dan melakukan kegiatan-kegiatan negatif lainnya di dalam dan luar lingkungan sekolah.
	18. Siswa dilarang membawa orang luar ke lingkungan sekolah tanpa seizin guru piket.
	19. Siswa dilarang keluar lingkungan sekolah pada jam pelajaran tanpa seizin guru piket.
	20. Siswa yang melanggar peraturan atau tata tertib diatas dengan sengaja maka akan dikenakan sanksi sebagai berikut:
		 – Teguran lisan atau surat peringatan 1, 2 dan 3 
		 – Surat panggilan kepada orang tua atau wali bila sudah diberi surat peringatan 3 kali.
		 – Skorsing
		 – Dikembalikan kepada orang tua atau wali murid.
	21. Setiap siswa harus menjaga nama baik sekolah baik di dalam maupun diluar lingkungan sekolah
	"""
	print(peraturan)

def option_d():
	d_tampilan()
	a = input("Pilih salah satu: ")
	if a == "5":
		system("cls")
		input("Press ENTER to return to MENU")
	elif a == "1":
		option1()
		input("Press ENTER to return to OPTION")
		option_d()
	elif a == "2":
		option2()
		input("Press ENTER to return to OPTION")
		option_d()
	elif a == "3":
		option3()
		input("Press ENTER to return to OPTION")
		option_d()
	elif a == "4":
		option4()
		input("Press ENTER to return to OPTION")
		option_d()
	else:
		print("INVALID Respond. Please try again...")
		input("Press ENTER to try again.")
		option_d()

def option_e():
	system("cls")
	Password = input("Code : ")
	if Password != "24353":
		system("cls")
		print("Wrong Password...")
		input("Press ENTER to return to MENU")
	else:
		for student in students:
			print("Nama:\t", student)
			print("Tanggal Lahir:\t", students[student]["Tg"])
			print("Tempat Lahir:\t", students[student]["Tl"])
			print("Nama ayah:\t", students[student]["Na"])
			print("Nama ibu:\t", students[student]["Ni"])
			print("Pekerjaan ayah:\t", students[student]["Ka"])
			print("Pekerjaan ibu:\t", students[student]["Ki"])	
			print("Telepon:\t", students[student]["Te"])
			print("Alamat:\t", students[student]["Al"])
			print("Asal Sekolah:\t", students[student]["As"])
			print("Agama:\t", students[student]["Ag"])
			print("Riwayat:\t", students[student]["Ri"])
			print("Persetujuan akan peraturan sekolah:\t", students[student]["Se"])
			print()
		input("Press ENTER to return to MENU")

def user_respond_check(lol):
	if lol == "A":
		option_a()
	elif lol == "B":
		option_b()
	elif lol == "C":
		option_c()
	elif lol == "D":
		option_d()
	elif lol == "E":
		option_e()
	elif lol == "F":
		pass
	else:
		print("INVALID Respond. Please try again.")
		input("Press ENTER to return to MENU.")

students = {
	'Marcello' : {
		"Tg" : "31 Mei 2006",
		"Tl" : "Palembang",
		"Na" : "Doni",
		"Ni" : "Wati",
		"Ka" : "Guru",
		"Ki" : "Guru",
		"Te" : "081234829485",
		"Al" : "Jln. Gang Surya",
		"As" : "Sekolah IGS",
		"Ag" : "Buddha",
		"Ri" : "Tidak ada",
		"Se" : "Setuju"
	}
}

user_respond = str()
while user_respond != "F":
	tampilan_menu()
	user_respond = input("Pilih Respond : ").upper()
	user_respond_check(user_respond)
else:
	system("cls")
	print("Thankyou for your cooperation and have yourself a nice day...")
	system("color 7")