x= int(input("Enter the starting number of the range: "))
y = int(input("Enter the ending number of the range: "))
prime = []
for n in range(x, y + 1):
    if n > 1:
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            prime.append(n)
print("Prime numbers are :", prime)

'''
Here we are taking input to start know where to start and end , basically giving a range .
Created an empty list named prime to store the output.
the for loop start from x and ends at y+1 as the it excluded the last element.
if n value is greater than 1 then is_prime is set to true another loop is used to check the if it is prime
or not where the range from 2 to n where if n is divisible by it will return zero which means it checks if
it has factors , so if it is divisible by i then it will return is_prime as false and break the loop
and if is_prime is true then it will append it in the empty list created.

'''