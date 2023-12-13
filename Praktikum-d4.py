print('Praktikum-d4')
print()

a = [2,3,1,0,3,1,1,1,6]
# akses item
print(a)
print(f'item indeks:0 {a[0]}')
print(f'item indeks:3 {a[3]}')
print(f'item indeks:terakhir {a[len(a)-1]}')
# akses item indeks negatif
print(f'item indeks:terakhir (-1) {a[-1]}')
print(f'item indeks:pertama (-9){a[-len(a)]}')
print(f'item indeks:1 (-8){a[-8]}')
print(f'item indeks:5 (-4){a[-4]}')
# akses indeks batas
print(f'item indeks:1,2,3 {a[1:4]}')
print(f'item indeks:1,2,... {a[1:]}')
print(f'item indeks:3,4,... {a[3:]}')
print(f'item indeks:0,1,2 {a[:3]}')
print(f'item indeks:0,1,2,3,4 {a[:5]}')
print(f'item indeks:semua {a[:]}')

# pengirisan indeks
print(f'item indeks:1,2,3 {a[1:4]}')
print(f'item indeks:2,3,4 {a[2:5]}')
print(f'item indeks:[1:8] {a[1:-1]}')

# Nested list
kelas = [('Pengantar Pemrograman',3),
          ('Pengantar Teknologi Informasi',3),
          ('Sains Terpadu',3)'
           ]
print(f'data kelas {kelas}')
kelas.append(('Pancasila',2))
# tambah matkul5 dan jumlah sks
print(f'data kelas {kelas}')
# Nama Mata kuliah 1: Pengantar Pemrograman dengan jumlah sks:3
# Nama Mata kuliah 2: Pengantar Teknologi Informasi dengan jumlah sks:3
# Nama Mata kuliah 3: Sains Terpadu dengan jumlah sks:3
# Nama Mata kuliah 4: Pancasila dengan jumlah sks:2
# Nama Mata kuliah 5: Pancasila dengan jumlah sks:3


data = [('Nurul Ainal Qalbi',2023,'Aktif'),
        (90,89,93,97),
        (20,22),
        ('S1-Reguler','Sistem Informasi D','Ganjil')]



# print(data[0][0])
# print(data[-1][0])
# print(data[2][0:])
