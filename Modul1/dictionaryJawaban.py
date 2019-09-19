# CRUD => Create , Read, Update, Delete

# d = {}

# d['Key'] = 'Value'
# d['Key1'] = 'Value1'
# d['Key2'] = 'Value2'

# d['key1']
# # for i in d:
# #     print(d[i])

# for i,j in d.items():
#     print(i)
#     print(j)

# UPDATE DICT

# dictionary = {
#     "namaDepan" : "fikri",
#     "namaBelakang" : "purwadhika",
#     "key2" : "value2"
# }

# dictionary['namaDepan'] = 'Fikra'


# # DELETE SATU ELEMENT

# del dictionary['namaDepan']
# print(dictionary)

# SEARCH KEY DICTIONARY

dictionary = {
    "namaDepan" : "fikri",
    "namaBelakang" : "purwadhika",
    "key2" : "value2"
}

dicari = 'n'
# print('n' in 'namaDepan')

for i in dictionary:
    # print(i)
    if((dicari in str(i)) == True):
        print(i + ' : ' + dictionary[i])
    
