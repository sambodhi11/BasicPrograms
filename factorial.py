x = int(input("Enter a number:"))
fact=1
for i in range(1, x+1):
    fact *= i
print("factorial is:", fact)

'''
factorial means it will multiply each element until the final number
suppose the number from user is 5 which means 1*2*3*4*5 = 120
the output should be 120
fact is 1 because any number multiplied by 0 will be zero.
for loop for the iteration which will start from 1 to x+1 which is x.
fact=fact*i can also be written as fact*=i which means each time i gets incremented it will
save that result in fact and that will again be multiplied with i.
Lastly , fact is printed.
'''