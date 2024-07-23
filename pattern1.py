n = 5  

for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')  
    for k in range(2 * i + 1):
        print('*', end='')  
    print()  

'''
Initializing n as 5 according to the pattern because there are 5 rows.
three for loops are used , the first for loop is for the rows which is n =5
second for loop is for the spaces.For eg: n-i-1 means 5-0-1 =4 will enter four spaces and for the
third loop k 2*0+1 =1 so 1 star/asterisk will get print .
print() will bring it to the next line , the same iteration goes on until it reaches to the end of n.
'''