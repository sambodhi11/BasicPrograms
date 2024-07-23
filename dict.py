from collections import OrderedDict
myDict = {'Ashwin': 100, 'rakesh': 9, 'Ravindra': 25, 'yash': 200, 'sai': 32}
sort = OrderedDict(sorted(myDict.items())) 
sorted_dict = OrderedDict(sorted(myDict.items(), key=lambda item: item[1]))
print(sort)
print(sorted_dict)
