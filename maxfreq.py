x= input("Enter a string:")
count={}

for i in x:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
result = max(count, key = count.get)
print("Maximum frequency is :",result)

'''
here taking input from user through variable x .Creating a dict named count to count with each key value pair.
2 loops where for i in x: start to iterate the string from x one by one .if i in count will again iterate and 
check if the element is present already in the dictionary.
count[i]+=1 will help to increment every time an element is repeated it will increment its count or else it will 
print 1 for that index value. 
result will give the element having the maximum freq in the count dictionary.
get is the key argument with the max function.Print function will give the character with maximum freq in the string.
'''