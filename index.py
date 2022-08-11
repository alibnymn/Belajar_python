# print ("Hallo")

# print("Hello World!")
# print("Hello Ali!")

# print("Belajar Python dari Nol")
# nama = "petani kode" 

# blok percabangan if
# if username == 'petanikode':
#     print("Selamat Datang Admin")
#     print("Silahkan ambil tempat duduk")

# # blok percabangan for
# for i in range(10):
#     print ("i")

# class Pagar:
#     """kelas pagar untuk membuat objek pagar. Dibuat oleh Petani Kode sebagai contoh saja."""
#     def __init__(self, warna, tinggi, bahan):
#         self.warna = warna
#         self.tinggi = tinggi
#         self.bahan = bahan

# # Mengakses dokumentasi kelas
# print (Pagar).__doc__
# input('\ntekan [enter] untuk melihat bantuan (dokumentasi) kelas: ')
# help(Pagar) # untuk melihat dokumentasi kelas

#  harga = 12000 #tipe int
# berat = 23.12 #float
# jarak = 3e3 #float 3000.0, huruf e artinya eksponen 10

# nama = "Ivan"
# jenis_kelamin = 'L'
# alamat = """
#     Jl. Suka Karya, No 32. RT Kode,
#     Kelurahan Mawar, Jakarta
# """
# agama = 'islam'

# Program bio data penduduk desa X
# membuat variabel beserta isinya (nilainya)
# nama = "Hartono"
# alamat = 'Mataram'
# umur = 19
# tinggi = 170.5
# menikah = False
# # mencetak isi variabel
# print ("Nama : ", nama )
# print ("Alamat : ", alamat )
# print ("Umur : ", umur )
# print ("Tinggi : ", tinggi )
# if(menikah):
#     print ("Status: menikah")
# else:
#     print ("Status: belum menikah")

# a = 10
# b = 3
# c = float(a) / float(b) #output: 3.3333333333333335

# print (c)

# Mengambil input
# nama = input("Siapa nama kamu: ")
# umur = input("Berapa umur kamu: ")

# # Menampilkan output
# print ("Hello",nama,"umur kamu adalah",umur,"tahun")

# nama = input("Nama: ")
# print ("Hello {} apa kabar?".format(nama))

# nama_mu = input("Nama kamu: ")
# nama_dia = input("Nama dia: ")

# print ("({} dengan {} sepertinya pasangan yang serasi :)".format(nama_mu, nama_dia)) 

# nama = input("Inputkan nama: ")
# umur = input("Inputkan umur: ")
# tinggi = input("Inputkan tinggi badan: ")

# print "Hello %s, saat ini usiamu %d tahun dan tinggi badanmu %f cm"(nama, umur, tinggi)

# file: operator_aritmatika.py

# # Ambil input untuk mengisi nilai
# a = input("Inputkan nilai a: ")
# b = input("Inputkan nilai b: ")

# # Menggunakan operator penjumlahan
# c = a + b
# print "Hasil %d + %d = %d" % (a,b,c)

# # Operator Pengurangan
# c = a - b
# print "Hasil %d - %d = %d" % (a,b,c)

# # Operator Perkalian
# c = a * b
# print "Hasil %d * %d = %d" % (a,b,c)

# # Operator Pembagian
# c = a / b
# print "Hasil %d / %d = %d" % (a,b,c)

# # Operator Sisa Bagi
# c = a % b
# print "Hasil %d %% %d = %d" % (a,b,c)

# # Operator Pangkat
# c = a ** b
# print "Hasil %d ** %d = %d" % (a,b,c)

# # file: operator_penugasan.py

# # Ambil input untuk mengisi nilai
# a = input("Inputkan nilai a: ")
# # ^ 
# # | contoh operator penugasan untuk mengisi nilai

# print "Nilai a = %d" % a

# # Coba kita jumlahkan nilai a dengan opertor penugasan
# a += 5
# # ^
# # |
# # contoh operator penugasan untuk menjumlahkan

# # Setelah nilai a ditambah 5, coba kita lihat isinya
# print "Nilai setelah ditambah 5:"
# print "a = %d" % a

# file: operator_pembanding.py
# a = input("Inputkan nilai a: ")
# b = input("Inputkan nilai b: ")

# # apakah a sama dengan b?
# c = a == b
# print ("Apakah %d == %d: %r" % (a,b,c)) 

# # apakah a < b?
# c = a < b
# print "Apakah %d < %d: %r" % (a,b,c)

# # apakah a > b?
# c = a > b
# print "Apakah %d > %d: %r" % (a,b,c)

# # apakah a <= b?
# c = a <= b
# print "Apakah %d <= %d: %r" % (a,b,c)

# # apakah a >= b?
# c = a >= b
# print "Apakah %d >= %d: %r" % (a,b,c)

# apakah a != b?
# c = a != b
# print "Apakah %d != %d: %r" % (a,b,c)

# a = True
# b = False

# # Logika AND
# c = a and b
# print ("%r and %r = %r" % (a,b,c))

# # Logika OR
# c = a or b
# print ("%r or %r = %r" % (a,b,c))

# # Logika Not
# c = not a
# print ("not %r  = %r" % (a,c))

# a = input("Masukan nilai a: ")
# b = input("Masukan nilai b: ")

# # Operasi AND
# c = a & b
# print "a & b = %s" % c

# # Operasi OR
# c = a | b
# print "a | b = %s" % c

# # Operasi XOR
# c = a ^ b
# print "a ^ b = %s" % c

# # Operasi Not
# c = ~a
# print "~a = %s" % c

# # Operasi shift left (tukar posisi biner)
# c = a << b
# print "a << b = %s" % c

# # Operasi shift right (tukar posisi biner)
# c = a >> b 
# print "a >> b = %s" % c

# umur = input("berapa umur kamu? ")
# aku = "bocah" if umur < 10 else "dewasa"
# print aku

# jomblo = True
# status = ("Menikah", "Single")[jomblo]
# print (status)

#Percabangan
# if lulus == "tidak":
#     print("kamu harus ikut remidi")

# lulus.py

# lulus = input("Apakah kamu lulus? [ya/tidak]: ")

# if lulus == "tidak":
#    print("Kamu harus ikut ujian")

# program untuk mengecek bonus dan diskon
# file: bonus.py

# total_belanja = input("Total belanja: Rp ")

# # jumlah yang harus dibayar adalah berapa total belanjaannya
# # tapi kalau dapat diskon akan berkurang
# bayar = total_belanja

# # jika dia belanja di atas 100rb maka berikan bonus dan diskon
# if total_belanja > 100000:
#     print("Kamu mendapatkan bonus minuman dingin")
#     print("dan diskon 5%")

#     # hitung diskonnya
#     diskon = total_belanja * 5/100 #5%
#     bayar = total_belanja - diskon


# # cetak struk
# print("Total yang harus dibayar: Rp %s" % bayar)
# print("Terima kasih sudah berbelanja")
# print("Datang lagi yaa...")

# cek_umur.py
# umur = input("Berapa umur kamu: ")

# if umur >= 18:
#     print("Kamu boleh membuat SIM")
# else:
#     print("Kamu belum boleh membuat SIM")

#file grade_nilai.py
# print("PROGRAM PYTHON MENENTUKAN NILAI INDEKS MAHASISWA")
# tugas = float(input("\nMasukkan nilai Tugas: "))
# uts = float(input("Masukkan nilai UTS: "))
# uas = float(input("Masukkan nilai UAS: "))

# na =  (0.15 * uas) + (0.35 * uts) +  (0.50 * uas)
# if na >= 80:
#     indeks = 'A'
# elif na >= 70:
#     indeks = 'B'
# elif na >= 55:
#     indeks = 'C'
# elif na >= 40:
#     indeks = 'D'
# else:
#     indeks = 'E'

# print("\nNilai Akhir  = %0.2f" % na)
# print("Nilai Indeks = %c" % indeks)

# file: perulanganFor.py

# ulang = 10

# for i in range(ulang):
#     print(f"Perulangan ke-{i}")

# item = ['kopi','nasi','teh','jeruk']

# for isi in item:
#     print(isi)

# jawab = 'ya'
# hitung = 0

# while(jawab == 'ya'):
#     hitung += 1
#     jawab = input("Ulang lagi tidak? ")

# print(f"Total perulagan: {hitung}")

# Kita punya list nama-nama buah
# buah = ["apel", "anggur", "mangga", "jeruk"]

# # Misanya kita ingin mengambil mangga
# # Maka indeknya adalah 2
# print (buah[2])

# # Buat list untuk menampung nama-nama teman
# my_friends = ["Anggun", "Dian", "Agung", "Adi", "Adam"]

# # Tampilkan isi list my_friends dengan nomer indeks 3
# print ("Isi my_friends indeks ke-3 adalah: {}".format(my_friends[3]))

# # Tampilkan semua daftar teman
# print ("Semua teman: ada {} orang".format(len(my_friends)))
# for friend in my_friends:
#     print (friend)

# Membuat list kosong untuk menampung hobi
# hobi = []
# stop = False
# i = 0

# # Mengisi hobi
# while(not stop):
#     hobi_baru = input("Inputkan hobi yang ke-{}: ".format(i))
#     hobi.append(hobi_baru)

#     # Increment i
#     i += 1
    
#     tanya = input("Mau isi lagi? (y/t): ")
#     if(tanya == "t"): 
#         stop = True


# # Cetak Semua Hobi
# print ("=" * 10 )
# print ("Kamu memiliki {} hobi".format(len(hobi)))
# for hb in hobi:
#     print ("- {}".format(hb))

# Membuat List
# todo_list = [
#     "Balajar Python",
#     "Belajar Django",
#     "Belajar MongoDB",
#     "Belajar Sulap",
#     "Belajar Flask"
# ]

# # Misalkan kita ingin menghapus "Belajar Sulap"
# # yang berada di indeks ke-3
# del todo_list[3]

# print (todo_list)

# # Beberapa list lagu
# list_lagu = [
#     "No Women, No Cry",
#     "Dear God"
# ]

# # playlist lagu favorit
# playlist_favorit = [
#     "Break Out",
#     "Now Loading!!!"
# ]

# # Mari kita gabungkan keduanya
# semua_lagu = list_lagu + playlist_favorit

# print (semua_lagu)

# List minuman dengan 2 dimensi

# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas

# # pemanggilan fungsi
# print ("Luas persegi: %d" % luas_persegi(6))

# membuat variabel global
# nama = "Petanikode"
# versi = "1.0.0"

# def help():
#     # ini variabel lokal
#     nama = "Programku"
#     versi = "1.0.2"
#     # mengakses variabel lokal
#     print ("Nama: %s" % nama)
#     print ("Versi: %s" % versi)


# # mengakses variabel global
# print ("Nama: %s" % nama)
# print ("Versi: %s" % versi)

# # memanggil fungsi help()
# help()

# fungsi untuk menampilkan menu
# Variabel global untuk menyimpan data Buku
# buku = []


# # fungsi untuk menampilkan semua data
# def show_data():
#     if len(buku) <= 0:
#         print ("BELUM ADA DATA")
#     else:
#         for indeks in range(len(buku)):
#             print ("[%d] %s" % (indeks, buku[indeks]))


# # fungsi untuk menambah data
# def insert_data():
#     buku_baru = input("Judul Buku: ")
#     buku.append(buku_baru)

# # fungsi untuk edit data
# def edit_data():
#     show_data()
#     indeks = input("Inputkan ID buku: ")
#     if(indeks > len(buku)):
#         print ("ID salah")
#     else:
#         judul_baru = input("Judul baru: ")
#         buku[indeks] = judul_baru

# # fungsi untuk menhapus data
# def delete_data():
#     show_data()
#     indeks = input("Inputkan ID buku: ")
#     if(indeks > len(buku)):
#         print ("ID salah")
#     else:
#         buku.remove(buku[indeks])

# # fungsi untuk menampilkan menu
# def show_menu():
#     print ("\n")
#     print ("----------- MENU ----------")
#     print ("[1] Show Data")
#     print ("[2] Insert Data")
#     print ("[3] Edit Data")
#     print ("[4] Delete Data")
#     print ("[5] Exit")
    
#     menu = input("PILIH MENU> ")
#     print ("\n")

#     if menu == 1:
#         show_data()
#     elif menu == 2:
#         insert_data()
#     elif menu == 3:
#         edit_data()
#     elif menu == 4:
#         delete_data()
#     elif menu == 5:
#         exit()
#     else:
#         print ("Salah pilih!")


# if __name__ == "__main__":

#     while(True):
#         show_menu()
#Fungsi lambda
# greeting = lambda name: print(f"Hello, {name}") 
# greeting("Dian")
# greeting("Ayu")

# bilangan = [10,2,8,7,5,4,3,11,0, 1]
# filtered_result = map (lambda x: x*x, bilangan) 
# print(list(filtered_result))

# # menentukan bilangan genap
# list(filter(lambda x: x%2 == 0, range(11)))
# [0, 2, 4, 6, 8, 10]

# Pembuatan fungsi
# def panggil(*nama):
#     print ("daftar orang yang dipanggil:")
#     for orang in nama:
#         print (orang)

# # pemanggilan fungsi
# panggil("dian", "deni", "agus")

# membuat fungsi rata-rata
def rata_rata(*data):
    banyak_data = len(data)
    jumlah_data = sum(data)
    nilai_rata_rata = float(jumlah_data) / float(banyak_data)
    return nilai_rata_rata

print (rata_rata(2,4,1,2,4,1,2,3,4,5,1,8,2))