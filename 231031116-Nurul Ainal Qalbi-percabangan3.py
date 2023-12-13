nama = input('Masukkan nama karyawan: ')
pendapatan = int(input('Masukkan pendapatan karyawan: '))
print('Nama karyawan:', nama)
print('Pendapatan:',pendapatan)

if pendapatan > 1000:
    print('Status: Berhak')
else:
    print('Status: Tidak Berhak')
