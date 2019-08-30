bulan = ['Jan' , 'Feb' , 'Maret']
print(bulan)
searchValue = input('Search : ')  # j
newList = [ item for item in bulan if searchValue.lower() in item.lower()]
# for item in bulan:
#     if (searchValue.lower() in item.lower()):
#         newList.append(item)
print(newList)






