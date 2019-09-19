
# import math
def remove_outlier(data) :
    dataSorted = sorted(data)
    mid = len(data) // 2  # 4
    data1 = dataSorted[0 : mid]
    data3 = dataSorted[-mid : ]
    q1 = data1[len(data1)//2] if len(data1) % 2 != 0 else (data1[len(data1) //2] + data1[(len(data1) // 2) -1]) / 2
    q3 = data3[len(data3)//2] if len(data3) % 2 != 0 else (data3[len(data3) //2] + data3[(len(data3) // 2) -1]) / 2
    iqr = q3 - q1
    lower_limit = q1 - 1.5*iqr 
    upper_limit = q3 + 1.5*iqr
    # print(lower_limit)
    # print(upper_limit)
    newData = []
    for item in data:
        if(item > lower_limit and item < upper_limit):
            newData.append(item)
    print('data asli adalah {}'.format(data))
    print('data Setelah di sort {}'.format(dataSorted))
    print('setengah data pertama {}'.format(data1))
    print('setengah data terakhir {}'.format(data3))
    print('upper Limit adalah  {}'.format(upper_limit))
    print('lower limit adalah  {}'.format(lower_limit))
    print('data yang tidak outlier adalah = {}'.format(newData))
# remove_outlier([71, 70, 73, 70, 70, 69, 70, 72, 71, 300, 71, 69])


def count_vowel (words):  #budi
    jumlah_vowel = 0
    vowel = ['a' , 'i' ,'u' , 'e' , 'o']
    for item in words:
        if(item.lower() in vowel):
            jumlah_vowel += 1
    print(jumlah_vowel)


# count_vowel('budi')

def given(arr):
    new_list = []
    for item in arr:
        for element in item:
            new_list.append(element)
    # SORT WITH BUBBLE SORT
    new_list.sort()
    print(new_list)


# given([[3, 2, 1], [4, 6, 5], [], [9, 7, 8]])


def countWords(words):
    wordsList = words.split(' ')
    countWords = {}
    for item in wordsList:
        if(item in countWords.keys()):
            countWords[item] += 1
        else:
            countWords[item] = 1
    for key, value in countWords.items():
        print("Jumlah kata '{}' ada sebanyak {}".format(key.capitalize() , value))

countWords('jangan jangan kamu adalah aku') 

# countWords = {'fikri' : 1}
# if(countWords['fikri']):
#     print('ada')







# GENAP
# arr = [1,2,3,4,5,6,7,8]    
# arr[0:((len(arr)//2) + 1)]
# arr[5:]

# # GANJIL
# arr = [1,2,3,4,5,6,7,8,9]  
# arr[0 : len(arr) // 2 + 1]
# arr[len(arr) // 2 + 2 : ]
