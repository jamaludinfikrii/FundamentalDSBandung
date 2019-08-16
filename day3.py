# FOR LOOP

# for item in range(3,10,2):
#     print('Urutan ' + str(item))


# item = 0
# while(item < 10):
#     print(item)
#     item += 1


#  NESTED LOOP

# out = ''
# for i in range(3):
#     for j in range(4):
#         out += '*'
#     out+= '\n'
# # out = '***\n***\n***\n'
# print(out)

# i = 0
# out = ''
# while(i<3):
#     j = 0
#     while(j < 4):
#         out += str(j + 1)
#         j += 1
#     out += '\n'
#     i += 1

# print(out)
# 1234
# 1234
# 1234
# 1234

# ****
# ****
# ****

# i = 3
# out = '1\n12\n123\n'
#j = 3
# while( i < 3): 
#     j = 0
#     while(j <= i):
#         out += str(j + 1)
#         j += 1
#     out += '\n'
#     i += 1

# print(out)

# LOOP FOR DRAWING
# out = ''
# for i in range(5):    ## i = 0,1,2,3,4
#     for j in range(i+1):
#         out+='*'
#     if(i ==4):
#         break
#     out+='\n'
# print(out)

i = 0
out = ''
num = 1
while(i < 5):
    j = 0
    while( j < (5-i) ):
        out += str(num) + ' '
        if(i == 0):
            out += ' '
        num = num + 2
        j += 1
    i += 1
    out += '\n'

print(out)



# Mau bikin apa? 1. Segitiga siku siku , 2. Segitiga sama kaki , 3. persegi
#                  1. ditanya =>  siku atas atau siku bawah
#                     berapa panjangnya = 5 (1-10)
#  *
#  **
#  ***
#  ****
#  *****

# ****
# ****
# ****
# ****