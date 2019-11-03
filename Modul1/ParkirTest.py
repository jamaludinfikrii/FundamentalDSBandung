# 1. Belanja 2. Belajar 3.Exit
# Kalo pilih Belanja munculin Menu => 1. Ayam Rp. 20000
#                                     2. Sapi Rp. 40000
#                                     3. Salmon Rp. 50000
# Berapa qty => 
# Output = totalharga
# Semua Input udah ada proteksi
# Setiap Selesai menu , ditanyain , mau ke menu awal atau enggak
# 
# 
# Kalo Pilih belajar => 1. Hitung Segitiga
#                       2. Hitung Trapesium
# hitung segitiga => input alas
#                 => tinggi
#                 luas =....
#                mau ke menu awal?

exit = False
while(exit == False):
    check = False
    while(check == False):
        menu = input('Mau Ngapain \n1. Belanja\n2. Belajar\n3. Exit')
        if(menu.isdigit()):
            menu = int(menu)
            if(menu > 0 and menu < 4):
                

        else:
            print('Anda Menginput Huruf, Tolong input angka')