'''
Misalkan anda diberikan tugas untuk membuat program struk pembelian pada kasir di perusahaan Alat Tulis Komputer (ATK). Pilih 5 barang Alat Tulis Kantor dengan harga masing-masing barang kemudian buatkan program dan ouputnya seperti berikut.

- Buat list data perusahaan
mdata = [PT. ABC Design,
        JL. BALAIKOTA NO.1,
        Kota Parepare,
        Nama Lengkap,
        mahasiswa@ith.ac.id,
        Nama Kasir,
        25 Oktober 2023]
(NOTED: ubah Nama Lengkap, e-mail, Nama Kasir, Tanggal-Bulan-Tahun Lahir)

- Buat Nested list untuk 5 barang:

djual = [['Barang1','Barang2','Barang3','Barang4','Barang5'],
        ['D0001','D0002','D0003','D0004','D0005'],
        [20,15,10,20,25],
        [2,2,2,2,2]]
(NOTED: ubah nama barang dan harga barang sesuai keinginan)

- Hasil Runing
                                 PT. ABC DESIGN
                          JL. BALAIKOTA NO.1 KOTA PAREPARE
                             e-Mail: mahasiswa@ith.ac.id


MANAJER           : Nama Lengkap
KASIR             : Nama Kasir
Tanggal Pembelian : 25 Oktober 2023
|--     16    --|--       19      --|--     15    --|--  8 --|--    14    --| 
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
No. Kode Barang |    Nama Barang    |   H. Satuan   | Jumlah |     Total    |
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
1   D0001       | Barang1           |      Rp27000,-|    2   |     Rp54000,-|
2   D0002       | Barang2           |      Rp75000,-|    2   |    Rp150000,-|
3   D0003       | Barang3           |      Rp12000,-|    2   |     Rp24000,-|
4   D0004       | Barang4           |      Rp10000,-|    2   |     Rp20000,-|
5   D0005       | Barang5           |       Rp3000,-|    2   |      Rp6000,-|
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                                    SUBTOTAL:           10   |    Rp254000,-|
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Summary:
Harga tertinggi adalah    : Rp75000,-  (D0002 - Barang2)
Harga terendah  adalah    : Rp3000,-   (D0005 - Barang5)
Harga rata-rata pembelian : Rp ,-
                                                   Parepare, 25 Oktober 2023
                                          



                                                         NAMA LENGKAP      
                                                         ------------
                                                            MANAJER

'''


# Write your code in below!

print('''
Nama\t\t: Nurul Ainal Qalbi
NIM\t\t: 231031116
Nomor Komputer\t: 00
Kelas\t\t: Sistem Informasi D''')

#Answer in below

mdata = ['PT. ABC Design',
        'JL. BALAIKOTA NO.1',
        'Kota Parepare',
        'Nurul Ainal Qalbi',
        'nurulainalq@gmail.com',
        'Jay J. Park',
        '09 Juli 2005']
djual = [['Pulpen','Buku','Stabilo','Type x','Mistar'],
        ['D0001','D0002','D0003','D0004','D0005'],
        [6000,10000,5000,3000,4000],
        [2,2,2,2,2]]

print('\n')
pjg = 16+19+15+8+14+5
print(f'{mdata[0].upper()}'.center(pjg))
print(f'{mdata[1]} {mdata[2].upper()}'.center(pjg))
print(f'''e-Mail: {mdata[4]}'''.center(pjg))
print('\n')
print(f'''MANAJER           : {mdata[3]}
KASIR             : {mdata[-2]}
Tanggal Pembelian : {mdata[-1]}''')
print('-'*(pjg))
print('No. Kode Barang'.ljust(16)+'|'+'Nama Barang'.center(19)+'|'+'H. Satuan'.center(15)+'|'+'Jumlah'.center(8)+'|'+'Total'.center(14)+'|')
print('-'*(pjg))
print(f'1   {djual[1][0]}'.ljust(16)+'|'+f' {djual[0][0]}'.ljust(19)+'|'+f'Rp{djual[2][0]},-'.rjust(15)+'|'+'2'.center(8)+'|'+f'Rp{djual[2][0]*2},-'.rjust(14)+'|')
print(f'2   {djual[1][1]}'.ljust(16)+'|'+f' {djual[0][1]}'.ljust(19)+'|'+f'Rp{djual[2][1]},-'.rjust(15)+'|'+'2'.center(8)+'|'+f'Rp{djual[2][1]*2},-'.rjust(14)+'|')
print(f'3   {djual[1][2]}'.ljust(16)+'|'+f' {djual[0][2]}'.ljust(19)+'|'+f'Rp{djual[2][2]},-'.rjust(15)+'|'+'2'.center(8)+'|'+f'Rp{djual[2][2]*2},-'.rjust(14)+'|')
print(f'4   {djual[1][3]}'.ljust(16)+'|'+f' {djual[0][3]}'.ljust(19)+'|'+f'Rp{djual[2][3]},-'.rjust(15)+'|'+'2'.center(8)+'|'+f'Rp{djual[2][3]*2},-'.rjust(14)+'|')
print(f'5   {djual[1][4]}'.ljust(16)+'|'+f' {djual[0][4]}'.ljust(19)+'|'+f'Rp{djual[2][4]},-'.rjust(15)+'|'+'2'.center(8)+'|'+f'Rp{djual[2][4]*2},-'.rjust(14)+'|')
print('-'*(pjg))
print(' '*17+' '*19+'SUBTOTAL:'.ljust(16)+f'{sum(djual[-1])}'.center(9)+'|'+f'Rp{sum(djual[-2])*2},-'.rjust(14)+'|')
print('-'*(pjg))
print('Summary:')
print(f'Harga tertinggi adalah    : Rp{max(djual[-2])},-   ({djual[1][1]} - {djual[0][1]})')
print(f'Harga terendah  adalah    : Rp{min(djual[-2])},-    ({djual[1][-1]} - {djual[0][-1]})')
print(f'Harga rata-rata pembelian : Rp{sum(djual[-2])/len(djual[-2])},-')
print(f'{mdata[2][5:]}, {mdata[-1]}'.rjust(pjg))
print('\n'*2)
print(f'{mdata[3].upper()}'.rjust(pjg-2))
bts = '-'*len(mdata[3])
print(bts.rjust(pjg-2))
print(f'{mdata[-2]}'.rjust(pjg-5))
