# COUNT WORD
def count_words(kalimat):
    stringArr = kalimat.split(' ')
    return len(stringArr)
    # return len(kalimat.split(' '))

# print(count_words('budi pergi ke pasar'))

# SMALL ENOUGH

def small_enough(a,b):
    total = 0
    for num in a:
        total+= num
    if total > b :
        print(False)
    else:
        print(True)

# small_enough([4,5,6,3,4,5,3,4] , 40)
# STRINGY
def stringy(num):
    i = 1
    hasil = ''
    while(i <= num):
        if(i % 2 != 0):
            hasil += '1'
        else:
            hasil += '0'
        i+=1
    print( int(hasil))

# stringy(5) 
# REMOVE DUPLICATES
def remove_duplicates(str):
    # bikin array kosong
    # string diubah ke array
    # looping di dalam stringArray
    # push ke dalam array kosong apabila kata belum ada di array kosong
    newArr = []
    strArr = str.split(' ')
    for i in strArr:
        if( i not in newArr ) :
            newArr.append(i)
    print(' '.join(newArr))

# remove_duplicates('alpha beta beta gamma gamma') 

def wave(a):
    hasil = [] 
    stringLower = a.lower()
    for i in range(len(stringLower)):
        a = list(a) #['h' ,'a' ,'i']
        a[i] = a[i].upper()
        hasil.append(''.join(a))
        a[i] = a[i].lower()

    print(hasil)

# wave('hai') 


# nama = list('fikri')
# nama[0] = nama[0].upper()

# print(''.join(nama))
# # cara akses string
# nama = 'fikri'
# nama[0]

# WAVE

# // capitalize("abcdef") => ['AbCdEf', 'aBcDeF']
def capitalize(a) :
    hasil = []
    a = a.lower()
    genap = ''
    ganjil = ''
    for i in range(len(a)):
        if(i % 2 ==0):
            genap += a[i].upper()
            ganjil += a[i]
        else:
            genap += a[i]
            ganjil += a[i].upper()
    hasil = [ganjil , genap]
    print(hasil)
    # ganjil = ''
    # for i in range(len(a)):
    #     if(i % 2 !=0):
    #         ganjil += a[i].upper()
    #     else:
    #         ganjil += a[i]
    # hasil.append(ganjil)
    # print(hasil)

# capitalize('abcdef')
# // reverseWords('budi pergi ke pasar') => 'rasap ek igrep idub'

def reverseWords(string):
    # arr = string.split(' ')
    # arr.reverse()
    # hasil = ''
    # for item in range(len(arr)):
    #     a = list(arr[item])
    #     a.reverse()
    #     hasil += ''.join(a)
    #     hasil += ' '
    # print(hasil)

    hasil = ''
    for i in range((len(string) -1) , -1 , -1):
        hasil += string[i]
    print(hasil)

# reverseWords('budi pergi ke pasar')

# // sortString("foos", "of")       => "oofs"
# // sortString("banana", "abn")    => "aaabnn"
# // sortString("fikri", "ikr")    => "iikrf"
# // sortString("purwadhika", "uhka")    => "uhkaaprwdi"

def sortString(toSort, sortBy):
    hasil = ''
    sortBy = list(sortBy)
    for i in range(len(sortBy)):
        for j in range(len(toSort)):
            if(toSort[j] == sortBy[i]):
                hasil += toSort[j]
    for i in range(len(toSort)):
        if(toSort[i] not in hasil):
            hasil += toSort[i]
    print(hasil)
sortString("foos", "of")
sortString("banana", "abn")
sortString("fikri", "ikr")


apasih()[1]()['key'] # ==> 'Fikri'


# // likes [] // must be "no one likes this"
# // likes ["Peter"] // must be "Peter likes this"
# // likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
# // likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
# // likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"


