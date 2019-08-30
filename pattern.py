
# a = 5
# hasil = ''
# if(a > 4 and a < 6):
#     hasil = 'Good'
#     if(a > 3 or a < 3):
#         hasil += 'Great'
#         if(a > 10 or a >= a):
#             hasil = 'Perfect'
        
    
# else:
#     hasil = 'Bad'

# print(hasil)


# angka = 0
# hasil = 0
# while angka >= 0 :
#     hasil+= angka
#     angka -= 1


# print(angka)



# -1



# hasil = 0
# nama = 'Purwadhika'
# hasil = 0
# for i in range(len(nama)):
#     hasil = i
#     # hasil = hasil + i


# # print(hasil) 9




# for i in range(0,10,-1):
#     print(i)



# jumlah = 0
# for item in range(1,11):
#     for j in range(item):
#         jumlah += 1
#         break
    
# # 9
# print(jumlah) 
# print(list(range(0)))

# i = 0
# out = 1
# while(i < 5):
#     j=0
#     while(j < i):
#         j -=1
#         out += j
#     i+=1
# print(out)


# Infinite loop




# SEGITIGA SAMA KAKI 5 Baris

#     *          1
#    ***         3
#   *****        5
#  *******       7
# *********      9

# JUMLAH SPASI
# Baris Pertama = jumlah baris -1    // 4
# Baris Kedua = (jumlah baris -1) -1 // 3
# Baris ketiga = (jumlah baris -1) -2 // 2
# SegitigaMaker(3)
#     1
#    234
#   56789

def SegitigaMaker():
    i = 1 #  i = 0   s = 4
    out = ''  # out = '    \n'
    # ganjil = 1
    while(i< 4):
        # SPACE
        s = 0
        while(s < (3 - i)):
            out += ' '
            s +=1
        # BINTANG
        b = 0
        while(b < (i*2)-1 ):
            out += '*'
            b +=1
        out += '\n'
        i+=1
    print(out)




SegitigaMaker()
