pwd_benar1 = 'si'
pwd_benar2 = '23'
pwd_benar3 = 'd'

limit = 3
i = 0
pwd1 = input('Masukkan Password Pertama: ')
while(pwd1 != pwd_benar1):
    i += 1
    if i == limit:
        print('Password salah, anda gagal pada halaman 1')
        break
    else:          
        pwd1 = input(f'''Password Salah!
Kesempatan anda tersisa {limit-i} kali
Masukkan Password Pertama: ''')
else:
    pwd2 = input('''Password Benar, Selamat Datang di halaman 1
Masukkan Password Ke-2: ''')
    
    i = 0
    while(pwd2 != pwd_benar2):
        i += 1
        if i == limit:
            print('Password salah, anda gagal pada halaman 2')
            break
        else:          
            pwd2 = input(f'''Password Salah!
Kesempatan anda tersisa {limit-i} kali
Masukkan Password Ke-2: ''')
    else:
        pwd3 = input('''Password Benar, Selamat Datang di halaman 2
Masukkan Password Ke-3: ''')
        
        i = 0
        while(pwd3 != pwd_benar3):
            i += 1
            if i == limit:
                print('Password salah, anda gagal pada halaman 3')
                break
            else:          
                pwd3 = input(f'''Password Salah!
Kesempatan anda tersisa {limit-i} kali
Masukkan Password Ke-3: ''')
        else:
            print('Password Benar, Selamat Datang di halaman 3')
