produk = ['Jeruk' , 'Kiwi' , 'Apel']
harga = [1000,2000,3000]


def printMenu():
    hasil = ''
    # hasil = '1. Jeruk Rp. 1000\n2. Kiwi Rp. 2000\n'
    for i in range(len(produk)):
        hasil += str((i+1)) + '. ' + produk[i]  +' Rp. ' + str(harga[i]) + '\n'
    # print(hasil)
    return hasil

def showProd():
    print(printMenu())

def inputData():
    newProd = input('Masukan Produk Baru?') 
    newPrice = input('Masukan Harga Dari {}?'.format(newProd))
    produk.append(newProd)
    harga.append(newPrice)
    print('Produk Berhasil Ditambah \n' + printMenu() )

def updateHarga():
    pilihProd = input('Pilih Produk yang mau di Update \n' + printMenu() + '\nPilih Salah satu: ' ) #1
    index = int(pilihProd) - 1
    newHarga = input('harga '+ produk[index] + ' Ingin diubah menjadi Berapa? : ') #100
    harga[index] = newHarga
    print('Produk Berhasil di ubah \n' + printMenu())

def deleteData():
    pilihProd = input('Pilih Produk yang mau di Delete \n' + printMenu() + '\nPilih Salah satu: ' ) #1
    index = int(pilihProd) - 1
    produk.pop(index)
    harga.pop(index)
    print('Produk Berhasil Di Hapus \n' + printMenu())
backToMenu = 'y'



while(backToMenu == 'y'):
    pilihMenu = input('1. Show Product \n2. Add Product\n3. Update Price\n4.Delete Product\nPilih salah satu : ') #1
    index = int(pilihMenu)-1 # 0
    menu = [showProd , inputData,updateHarga,deleteData]
    menu[index]()
    backToMenu = input('Kembali Ke Menu Utama? (y)')


