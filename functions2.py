# VARIABEL
# harga1 = 20000


# # PENGKONDISIAN
# # operator comparison 
# # operator aritmatika +
# if(1 > 0):
#     action
# # LOOPING

# while(condition):
#     action
# for i in range(1,20,2)
# FUNCTION


# Declare Func => bikin function
# Call Func => Make Function

# hapusVokal('fikri')

# checkPlatNomor('D 1 AB') => 'Kendaraan Boleh Lewat'

# nama = 'fikri'

# SLICE STRING

# plat =  'D 6543 AB'
# print(plat[5:6] + 'halo') 
# print(nama[0])

def checkPlatNomor(plat) :
    import datetime 
    x = datetime.datetime.now()
    tanggal = str(x.date())
    tanggal = tanggal[-2:]

    platNomor = plat.split(' ')[1]
    # if((int(tanggal) % 2 ==0 and int(platNomor) % 2 == 0) or (int(tanggal) % 2 !=0 and int(platNomor) % 2 != 0)  ):
    if((int(tanggal) % 2 == 0) == (int(platNomor) % 2 == 0)):
        print('Kendaraan Boleh Lewat')
    else:
        print('Kendaraan tidak boleh lewat')


checkPlatNomor('B 121312 AB')

# ALGORITMA => LANGKAH LANGKAH UNTUK MENYELESAIKAN MASALAH
# 3 * 5
# 3 dijumlahkan dengan 3 sebanyak 5 kali
# 5 dijumlahkan dengan 5 sebanyak 3 kali
# 3 * 5


# MEMPERTIMBANGKAN 2 HAL speed and space

def dupString(stringToDuplicate): #abc => abbccc
    hasil = ''
    for i in range(len(stringToDuplicate)): # i = 1
        for j in range(i+1): # j = 0
            hasil += stringToDuplicate[i]
    # hasil += stringToDuplicate[0]
    # hasil += stringToDuplicate[1]
    # hasil += stringToDuplicate[1]
    # hasil += stringToDuplicate[2]
    # hasil += stringToDuplicate[2]
    # hasil += stringToDuplicate[2]
    print(hasil)

dupString('abc')


# for i in range(5):
#     for j in range(3):
#         print('Ini Nested Loop ke = ' + str(j))
#         for k in range(2):
#             print('Ini Nested Nested Loop ke = ' + str(k))
#     print('======================')    
    

# print('Ini Nested Loop ke = ' + 0)
# print('Ini Nested Nested Loop ke = ' + 0)
# print('Ini Nested Nested Loop ke = ' + 1)
# print('Ini Nested Loop ke = ' + 1)
# print('Ini Nested Nested Loop ke = ' + 0)
# print('Ini Nested Nested Loop ke = ' + 1)
# print('Ini Nested Loop ke = ' + 2)
# print('Ini Nested Nested Loop ke = ' + 0)
# print('Ini Nested Nested Loop ke = ' + 1)

def SegitigaMaker(baris):
    i = 1 #  i = 0   s = 4
    out = ''  # out = '    \n'
    angka = 1
    # ganjil = 1
    while(i< baris):
        # SPACE
        s = 0
        while(s < ((baris-1) - i)):
            out += ' '
            s +=1
        # BINTANG
        b = 0
        while(b < (i*2)-1 ):
            
            out += str(angka)
            # if(i < 4):
            #     out += '  '
            # else:
            #     out += ''
            angka += 1
            b +=1
        out += '\n'
        i+=1
    print(out)


# 





SegitigaMaker(5)