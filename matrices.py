X = [[1,2,3],
    [4,5,6],
    [7,8,9]]

Y = [[1,2,3],
    [4,5,6],
    [7,8,9]]


result = [[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range(len(X)):   
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]

for r in result:
    print(r)

for c in range(len(X)):   
    for d in range(len(X[0])):
        result[c][d] = X[c][d] - Y[c][d]

for k in result:
    print(k)

'''
Here I have assigned two variables for addition and subtraction with 3x3 matrix.
and another matrix called result for saving the addition and subtraction of the the matrices.
have used 2 loops for addition and 2 other for subtraction.
The first for loop is for the rows and the second for loop is for the columns.
It will start iteration from x[0] means it will start from the 0th index value.
then result [i][j]=x[i][j]+y[i][j] will add from the i th and the j th position from and add .
the very same the loops for subtraction will work.
and the result will be printed .
'''