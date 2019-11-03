# def getSquared(num):




def getSquared(angka):
    angka_list = str(angka)
    hasil = ''
    for i in range(len(angka_list)):
        hasil += str(int(angka_list[i]) * int(angka_list[i]))
    print(hasil)

getSquared(3334)

def filterFriend(a):
    myFriend = []
    for i in a:
        if(len(i) == 4):
            myFriend.append(i)
    print(myFriend)

arr = ["Ryan", "Kieran", "Jason", "Yous"]
filterFriend(arr)


def domainName(terserah):
    list_domain = terserah.split('.') # => ['https://www' , 'cnet' , 'com']
    if(len(list_domain) == 3):
        print(list_domain[1])
    elif(len(list_domain) == 2):
        print(list_domain[0].split('//')[1])

# alamat = 'jl. trunojoyo no 11 , bandung , 5512'
domainName("https://www.cnet.com") 
domainName("http://github.com/carbonfive/raygun") 
domainName("http://www.zombie-bites.com")




# filterFriend(["Ryan", "Kieran", "Jason", "Yous"])  => ['Ryan' , 'Yous']

# domainName("http://github.com/carbonfive/raygun") == "github"
# domainName("http://www.zombie-bites.com") == "zombie-bites"
# domainName("https://www.cnet.com") == "cnet"

# countWords('Budi Pergi Ke Pasar') => 4


# smallEnough([66, 101], 200) ==> True
# smallEnough([78, 117, 110, 99, 104, 117, 107, 115], 100)  => False # Dilarang Pake sum()

# removeDuplicats('alpha beta beta gamma gamma') => 'alpha beta gamma'

# stringy(12) => 101010101010
# stringy(3) => 101
# stringy(4) => 1010

# wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
# wave("hai") => ['Hai' , 'hAi' , 'haI']

# likes [] // must be "no one likes this"
# likes ["Peter"] // must be "Peter likes this"
# likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
# likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
# likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"


    