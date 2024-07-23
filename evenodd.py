even =[]
odd =[]
for n in range (0,101):
    if n %2 ==0:
        even.append(n)
    else:
        odd.append(n)
print("even numbers :", even)
print("Odd numbers:" ,odd)

'''
Creating 2 separate blank list for the even and odd.
for loop used to iterate from the given range. If the vlaue iterating from 0 to 101 is divisible by 2 and
returns remainder as 0 then it is an even number so using append function will append/add the even number in 
the even list. Same for odd but here even if it divisible and returns a non zero value then it is considered as 
odd. So append this in the blank list of odd.
At last printing both the list which now have the even n odd numbers.
'''