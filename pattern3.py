n= 5
for i in range(n+1,0,-1):
    for j in range(0,i-1):
        print("*", end="")
    print("")
    
'''
Same as before here the whole pattern is reversed , this can be done by giving 2 for loops , the iteration 
will start from 6 as we need the pattern to be reversed and end to 0 which is excluded,
For i in range(n+1, 0,-1) which means the iteration will start from n+1 which is 6 and will stop at 0 which is excluded and the -1
which means the loop will run in descending order that is from  6 to 1.
For j in range (0,i-1) which means the range will go from 0 to i-1 as the iteration of I will start 
from 6 so 6-1 =5 so it will go in decrementing the value upto 0.
'''