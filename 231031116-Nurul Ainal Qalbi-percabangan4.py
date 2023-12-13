pendapatan = int(input('Masukkan pendapatan: '))
if pendapatan <= 1000:
    persentase = 10
elif pendapatan <= 2000:
    persentase = 20
elif pendapatan <= 3000:
    persentase = 30
elif pendapatan <= 4000:
    persentase = 40
else:
    persentase = 50

bonus = pendapatan * (persentase / 100)
total = pendapatan + bonus

print('Pendapatan:',pendapatan)
print('Persentase',persentase)
print('Bonus',bonus)
print('Jumlah Total:',total)
