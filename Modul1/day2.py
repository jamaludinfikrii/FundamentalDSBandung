# ASSIGNMENT OPERATOR

# a = 5
# b = a
# # print(b)

# # b+= a # b = b + a
# b *= a
# nama = 'Fikri '
# nama += 'Jamaludin'
# print(nama)

# print(b)


# COMPARISON

# if(boolean):
#   action

# COMPARISION OPERATOR menghasilkan boolean

# LOGICAL OPERATOR
# and 
# or
# not

# and ==> DUA DUANYA HARUS TRUE BARU BERNILAI TRUE
# or ==> SALAH SATU TRUE BERNILAI TRUE
# not ==> Kebalikannya

# angka = 5
# print(angka == 5 or angka < 4)


# massa = int(input('Masukan Massa Badan(kg) ?'))
# tinggi = int(input('Masukan tinggi Badan(cm) ?')) / 100
# imt = massa / (tinggi*tinggi)
# hasil = 'imt anda adalah ' + str(imt) + 'Berat Badan '
# if(imt < 18.5):
#     hasil += 'Kurang'
# elif( imt >= 18.5 and imt <25):
#     hasil += 'Ideal'
# elif( imt >= 25 and imt <30):
#     hasil += 'Berlebih'
# elif( imt >= 30 and imt <40):
#     hasil += 'Sangat Berlebih'
# elif( imt >= 40):
#     hasil += 'Obesitas'
# print(hasil)



# if(condition:boolean ):
#    action
# elif(condition : boolean):
#    action
# else:
#    action



#  LOOPING // PENGULANGAN // ITERATION
#  Kembangan Dari Pengkondisian
#  KALAU IF KONDISION TRUE DIA JALAN SEKALI
#  KALAU LOOP SELAMA KONDISI TRUE DIA BAKAL JALAN TERUS (MENGULANG)
#  INFINITE LOOP
#  MAKANYA HARUS SELALU DIBIKIN EXIT WAY
# angka = 0
# while(angka > 10):
#     print(angka)
#     angka+= 1






# jumlah = 0
# angka = 1
# while(angka < 5):
#     print(jumlah) 
#     jumlah += angka
#     angka += 1

# jumlah = 10
# angka = 5

# terminal
# 0
# 1
# 3
# 6



# angka = 10
# jumlah = 0
# while(angka > 0):
#     jumlah += angka
#     angka += 1
#     if(angka ==11):
#         break

# print(jumlah) 






i = 10
out = ''
while(i > 0):
    out += str(i)
    if(i == 1):
        break
    out += ','
    i -= 1
print(out)
# out = 10,9,8,7,6,5,4,3,2,1,