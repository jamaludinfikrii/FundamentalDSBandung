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




removeVocal('Fikri') => 'fkr'
check('Fikri' ,'a') => False
oddEven(9) => 9 adalah ganjil
maxNumber(3,5,1,11) => 11
stringFilter('asddsa123') => 123
checkPlatNomor('D 5567 GA') => plat nomor
# // 1. Function utk hapus huruf vocal v => Senin sebelum jam 8
# // 2. Function check v
# // 3. Function ganjil genap v
# // 4. Function display angka terbesar v
# // 5. Function ngefilter string (hanya bisa integer) v
# // 6. Check Plat Nomor v


