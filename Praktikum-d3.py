nama = 'Nurul Ainal Qalbi'
nim  = '231031116'
prodi= 'Sistem Informasi D'
meet = 'Praktikum 3'
email= 'nurulainalq@gmail.com'

sp = 40
# print(len(nama))
print('-'.center(sp,'-'))
print(nama.center(sp))
print(nim.center(sp))
print('\n'*2)
print(meet.rjust(sp))
print(prodi.rjust(sp))
print(email.rjust(sp))
print('-'.center(sp,'-'))

paragraf = '''\tHalo, selamat datang perkenalkan
nama saya {} dengan NIM {} dari prodi {}.
Ini adalah file {}.'''

p = paragraf.format(nama,nim,prodi,meet)
print(p)

# ---------5++++++++9---------
# 1. input nilai x
x = int(input('Masukkan Nilai ---5++++9---- = '))
print(x)

# 2. cek1 apakah x>5 true
cek1 = x>=5
# 3. cek2 apakah x<9 true
cek2 = x<=9 
# 4. status = cek1 dan cek2
status = cek1 and cek2
# 5. cetak status
print('Hasilnya adalah',status)

# +++++++5--------9++++++
# 1. input x
x = int(input('Masukkan Nilai ++++5---9++++ = '))
# 2. cek1 apakah x>5 true
cek1 = x<=5
# 3. cek2 apakah x<9 true
cek2 = x>=9 
# 4. status = cek1 dan cek2
status = cek1 or cek2
# 5. cetak status
print('Hasilnya adalah',status)

# +++++++5--------9++++++13-------
# 1. input x
x = int(input('Masukkan Nilai ++++5---9++++ = '))
# 2. cek1 x<5 
cek1 = x<5
# 3. cek2 x>9 
cek2 = x>9 
# 4. cek3  x<13 
cek3 = x<13
# 5. status cek1 or cek2 and cek3
status = cek1 or cek2 and cek3
# 6. cetak status
print('Hasilnya adalah',status)

# -----5++++++9------13++++++16
# 1. input x
x = int(input('Masukkan Nilai 5++++++9------13++++++16= '))
# 2. cek1 x>5 
cek1 = x>5
# 3. cek2 x<9 
cek2 = x<9 
# 4. cek3  x>13 
cek3 = x>13
# 5. cek4 x<16
cek4 = x<16
# 6. status cek1 or cek2 and cek3 or cek4
status = cek1 or cek2 and cek3 or cek4
# 7. cetak status
print('Hasilnya adalah',status)

#Tugas 1
# -----5++++++9------13++++++16--------

#Tugas 2
# +++++5-----9+++++13-----16+++++

#Tugas 3
# -----5++++++9------13++++++16--------20+++++24----

#Tugas 4
# -----5++++++9------13++++++16--------20+++++24
