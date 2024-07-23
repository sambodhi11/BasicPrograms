i = int(input("enter a number:"))
rev=0
temp = i
while i>0:
    n = i % 10
    rev = rev * 10 + n
    i = i //10
if temp == rev:
    print("True")
else:
    print("False")

'''
taking input from user to enter a number to check whether it is palindrome or not.
rev stands for reverse which is set to 0 . 
temp=i is used store the value of i temporarily.
while loop is used, where i value should be greater than 0 
where n will store the  result of i%10 this will return the remainder in n.
rev  will save the result of rev*10+n which means 0*10+n whatever the n is. and then again divide it by 10.
keep doing it until it is indivisible.
if the number returns and be the same number then its a palindrome number and it will return true or else it will 
return false .
'''