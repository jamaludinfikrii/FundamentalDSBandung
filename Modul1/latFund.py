# p0 = penduduk awal ,  percent = increase percent every year
# aug = new inhabitans, p = target
# def nb_year(p0,percent,aug,p):
#     penduduk = p0
#     tahun = 0
#     while(penduduk < p):
#         penduduk = penduduk + (5/100 * penduduk) + aug
#         tahun += 1
#     print(tahun)
# print(nb_year(1500,5,100,5000) + 14)


# RETURN VALUE
# def fn():
#     return [0,5,{'makan' : lambda : lambda x : print('Hello ' + x)}]

# fn()[2]['makan']()('fikri')  ## Hello Fikri

# def x ():
#     return {'nama' : lambda :lambda : [0,1,lambda a,b : print(a+b)]}

# x()['nama']()()[2](2,2) ## 4

# a = lambda x,y,z : 'fikri'
# def a (x,y,z):
#     return x + y + z


# 1500
# 5%
# 100
# 5000



def tickets(peopleInline):
    m25,m50,m100 = 0 , 0, 0
    for item in peopleInline:
        if(item == 25):
            m25 += 1
        elif(item == 50):
            m25 -= 1
            m50 += 1
        elif(item == 100):
            m100 += 1
            m25 -= 1
            if(m50 > 0):
                m50 -= 1
            else :
                m25 -=2
    
    if(m25 < 0 or m50 < 0):
        print('NO')
    else:
        print('YES')
# tickets([25,25,50,100,100]) # YES


def rowSumOddNumber(baris) :
    out = ''
    angka = 1
    total =0
    for i in range(baris):
        out += ' ' *((((baris-1) -i) * 2))
        for j in range(i + 1):
            out += str(angka)
            if(angka < 10):
                out += '   '
            else :
                out += '  '
            if( i == baris-1):
                total += angka
            angka += 2
        out += '\n'
        
    # print(out)
    # print(total)

# rowSumOddNumber(3)







# alphaSum('fik') => '6 + 9 + 11 = 26'

alphabet = list('abcdefghijklmnopqrstuvwxyz')
# alphabet = ['a','b','c','d']

def alphaSum(a):
    index = []
    for i in range(len(a)):
        indexAlpha = alphabet.index(a[i])
        index.append(indexAlpha + 1)
    hasil = ''
    total = 0
    for i in range(len(index)) : 
        hasil += str(index[i]) 
        total += index[i]
        if(i == len(index) -1):
            hasil += ' = '
            hasil += str(total)
        else :
            hasil += ' + '
    print(hasil)
# alphaSum('abc')



# alphaNext('abc' , 2) => 'cde'
# alphaNext('abc' , 1) => 'bcd'
# alphaNext('zzz' , 1) => 'aaa'

def alphaNext(alpha , numNext):
    # Cari tau param alpha ada di index ke berapa dari list alphabet
    # Setiap Ketemu, masukin ke list
    index = [] # [0,1,2]
    indexSetelahDijumlah = [] # [2,3,4]
    for i in range(len(alpha)):
        index.append(alphabet.index(alpha[i]))
    for item in index:
        indexJumlah = item + numNext
        if(indexJumlah > 25):
            indexJumlah = indexJumlah % 26
        indexSetelahDijumlah.append(indexJumlah)
    hasil = ''
    # print(indexSetelahDijumlah)
    for item in indexSetelahDijumlah: 
        hasil += alphabet[item] 
    print(hasil)


# alphaNext('zzz' , 2)
































# myGloves = ['red','green','red','blue','blue' , 'blue'];

# numberOfPairs(myGloves) == 2;



# alphabet = list('abcdefghijklmnopqrstu')
# maju = 'a' 
# index = alphabet.index(maju)
# print(alphabet[index + 10])

import math
def numberOfPairs(myGloves):
    gloves = {} #{'red' : 2 , 'green' : 1 , 'blue' : 1}
    for item in myGloves:
        if item in gloves.keys():
            gloves[item] += 1
        else :
            gloves[item] = 1
    pairs = 0
    for item in gloves.values():
        pairs +=math.floor(item/2)
    print(pairs)
# numberOfPairs(myGloves)














# myGloves = ['red','green','red','blue','red','red']
# pairs = 0
# for i in range(len(myGloves)):
#     for j in range(i+1, len(myGloves)):
#         if(myGloves[i] == myGloves[j]):
#             pairs += 1
#             myGloves.pop(i)
#             myGloves.pop(j)
#             break

def count_pairs(myGloves):
    i = 0
    pairs = 0
    while(i < len(myGloves)):
        
        j = i+1
        cocok = False
        while(j < len(myGloves) ):
            if(myGloves[i] == myGloves[j]):
                pairs += 1
                myGloves.pop(j)
                myGloves.pop(i)
                cocok = True
                break
            j+=1
        if(cocok == True):
            i = 0
        else :
            myGloves.pop(i)
            i = 0
    print(pairs)
# myGloves = ['red','green','red','blue','red','red','blue','green'] ##['green' , 'blye' , 'red' , 'red']
# myGloves2 = ['black' , 'green' , 'blue' , 'yellow' , 'red' , 'red']
 
# count_pairs(myGloves)





















# print(gloves)
# myGloves = {
#     'red' : 2,
#     'green' : 2
#     'blue' : 4
# }
# myGloves = [
#     ['red' , 2],
#     ['green' , 2],
#     ['blue' : 2]
# ]


# numberOfPairs(myGloves) 














def generateNum(data):
    bulan = 'jan feb mar apr mei juni juli agust sept okt nov des'.split(' ')

    hasil = ''
    hasil+= data[3]
    hasil+= data[0][0].upper()
    hasil+= data[1][0].upper()
    lenNama2 = len(data[1])
    lenNama2Set = math.floor((lenNama2/2))
    lenNamaSet = lenNama2//2
    hasil += data[1][lenNama2Set].upper() if( lenNama2 % 2) != 0 else  (data[1][lenNamaSet-1] + data[1][lenNamaSet]).upper()
    hasil += '-'
    hasil += data[2][1]
    hasil += str(bulan.index(data[2].split('-')[1].lower()) + 1)
    hasil += data[2][-2:]
    print(hasil)

# data = ["John","Smith","01-Jan-1967","M"]
# data2 = ["Steve","Jobs","23-Jan-2010","M"]
# generateNum(data2)
# 
# a = 5
# b = 'good' if a > 3 else 'bad'
# print(b)
















# generateNum(data)  ==> 'MJSI-1167'
# generateNum(data2)  ==> 'MSJOB-3110'




# findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2

def findUniq(data):
    num = {}
    for item in data : 
        if(item in num.keys()):
            num[item] += 1
        else:
            num[item] = 1
    uniq = []
    for key,value in num.items():
        if(value == 1):
            uniq.append(key)
    hasil = 'yang uniq adalah '
    for item in range(len(uniq)):
        hasil += str(uniq[item])
        if(item == len(uniq) - 2):
            hasil += ' dan '
        else :
            if(item != len(uniq) -1):
                hasil += ','
    print(hasil)


# findUniq([ 1, 2, 1, 2, 1, 1 ]) === 'Nothing'
# findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55

def sumTwoSmallest(data):
    data = [19, 5, 42, 2, 77]
    data.sort()
    print(data[0] + data[1])

# data =[3,3,2,2,6,5]
# total = 0
# for item in data:
#     if(item % 2 != 0):
#         total+= item
# print(total)



















# REVIEW

# print(3//3)
# hasil = 'yang unik adalah {noe}'.format(noe = '2')


# print(hasil)


# ls = [4,5,3,5,3,4,5]
# print(ls[-5 : ])

# nama = 'purwadhika'
# print(nama[-3 :])

d = {
    '1' : 2,
    '2' : 3,
    '3' : 1
}

# d['key'] = 'a'
# a = d.copy()
# d.pop('key')
# print(d)
# print(a)
# nama = 'fikri'
# num = -1
# if(!num) : 
#     print(True)


# findEven([1, 2, 3, 4, 5, 6, 7, 8, 9],  3) => [4, 6, 8]
# findEven([-22, 5, 3, 11, 26, -6, -7, -8, -9, -8, 26],  2) =>  [-8, 26]
# findEven([6, -25, 3, 7, 5, 5, 7, -3, 23], 1) => [6]

# 150 / 1.5 = 100




# sumOdd() ==> 11
# sumOdd([1,3,2,1,8,5]) ==> 10


