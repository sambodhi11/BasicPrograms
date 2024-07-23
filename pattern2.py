n = 5
for i in range (1, n+1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()
    
'''
n =5 is already assigned for 5 rows.
2 for loops are used one for the rows and the other for the columns.
the first loop will start iteration from 1 till n+1 means 5+1=6 because range excludes the last element.
for the second loop it will iteration from 1 and end when the first iteration will end, so if i =1 it will 
print 1 star ,and move to the next line. when i value becomes 2 , j will print from 1 to2 which means 2 stars,
again move to the next line.
This iteration will work until it reaches the end of the loop.
'''