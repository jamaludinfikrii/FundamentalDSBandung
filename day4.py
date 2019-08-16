# FUNCTION 

# def NamaFunc():
#     prog

# def contoh():
#     print('Hello World')


# contoh()
# contoh()
# contoh()

# FUNCTION WITH PARAMETER

# def blender(buah):
#     print('jus ' + buah)

# blender(buah = 'Apel')
# blender(buah = 'Jeruk')

# # 
# def HitungParkir(masuk,keluar):
#     totalJam = abs(keluar - masuk)
#     totalBiaya = totalJam * 3000
#     print(totalBiaya)

# HitungParkir(masuk=7 , keluar=10)
# HitungParkir(7,12)



# def removeChar(a,b):
#     # oldstring = a
#     # charToRemove = b
#     # newString = oldstring.replace(charToRemove , '')
#     # print(newString)
#     print(a.replace(b, ''))

# removeChar('Fikri' , 'i')
# removeChar('purwadhika' , 'i')

# # batuKertasGunting('Kertas' , 'Gunting') # Player 2 menang

def batuKertasGunting(player1,player2):
    if(player1 == player2):
        print('Seri')
    elif(player1 == 'Kertas'):
        if(player2 == 'Gunting'):
            print('Player 1 memilih {}, dan player 2 memilih {}, player 2 menang '.format(player1 , player2))
        elif(player2 == 'Batu'):
            print('Player 1 memilih {}, dan player 2 memilih {}, player 1 menang '.format(player1 , player2))
    elif(player1 == 'Batu'):
        
batuKertasGunting('Kertas' , 'Batu')



# nama = 'Fikri'
# b ='Purwadhika'
# s = 'Nama Saya {} , {}'.format(b,nama)
# print(s)
