row=int(input("Enter the number of rows: "))
column=int(input("Enter the number of columns: "))

# Initialize matrix
matrix = []
print("Enter the entries rowwise:")
  
# For user input
for i in range(row):          # A for loop for row entries
    a =[]
    for j in range(column):      # A for loop for column entries
         a.append(int(input()))
    matrix.append(a)
  
# For printing the matrix
for i in range(row):
    for j in range(column):
        print(matrix[i][j], end = " ")
    print()

currentRow = currentColumn = z = 0

n=row if row > column else column
z=0

while(row>0 or column>1):
    if(n>0):
        for i in range (column): 
            print(matrix[currentRow][currentColumn])
            if(z):
                currentColumn-=1
            else:
                currentColumn+=1
        if(z):
            currentColumn+=1
            row-=1
            currentRow-=1
        else:
            currentColumn-=1
            row-=1
            currentRow+=1

    if(n>1):
        for j in range (row):
            print(matrix[currentRow][currentColumn])
            if(z):
                currentRow-=1
            else:
                currentRow+=1
        if(z):
            currentRow+=1
            column-=1
            currentColumn+=1
        else:
            currentRow-=1
            column-=1
            currentColumn-=1

        n-=1
        if(z):
            z=0
        else:
            z=1
