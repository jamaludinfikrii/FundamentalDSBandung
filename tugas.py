import math
apa = input('Mau Menghitung Apa ? (1). Hari atau  (2). Detik? : ')
if(apa == '1'):
    hari = input('Berapa Hari? : ')
    hari = int(hari)
    tahun = math.floor(hari / 360)
    sisahari = hari%360
    bulan = math.floor(sisahari / 30)
    sisahari = sisahari % 30
    print(str(hari) + ' hari, sama dengan ' + str(tahun) + ' tahun, ' + str(bulan) + ' bulan ' + str(sisahari) + ' hari')
    