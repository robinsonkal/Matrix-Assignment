## MATRIX CLASS ASSIGNMENT
##Kaleb Robinson


def listoflists(matrix):##function that converts the matrix input into the matrix list
    matrixlist=[]
    counter=0
    rowlist=[]
    num=""

    for i in matrix:
        counter+=1
        if i.isdigit() or counter==len(matrix):
            num=num+i
        if i==" ":
            rowlist.append(int(num))
            num=""
        if i=="/" or counter==len(matrix):
            rowlist.append(int(num))
            matrixlist.append(rowlist)
            rowlist=[]
            num=""
    return matrixlist



class Matrix():

    ## Initialize a Matrix object with an input matrix, stored as a list-of-lists.
    def __init__( self, matrix1, other ):
        self.matrix1=matrix1
        self.other=other
        self.matrix1dim=[]
        self.otherdim=[]
        matrix1row=self.get_row(matrix1)
        matrix1col=self.get_col(matrix1)
        otherrow=self.get_row(other)
        othercol=self.get_col(other)
        self.matrix1dim.extend([matrix1row,matrix1col])
        self.otherdim.extend([otherrow,othercol])
        self.add()
        self.sub()
        self.mult()
        self.transpose()

    def get_row( self,matrix ):#gets row of passed matrix
        i=0
        for l in matrix:
            i+=1
        return i

    def get_col(self,matrix):#gets column of passed matrix
        counter2=0
        counter1=0
        columncheck=[]
        for i in matrix:
            for k in matrix[counter1]:
                counter2+=1
            columncheck.append(counter2)
            counter2=0
            if counter1>=1 and columncheck[counter1]!=columncheck[counter1-1]:
                print("column is uneven")
                ##TODO what to do if column is uneven
            counter1+=1
        return columncheck[0]

    def add( self):##adds matrix1 and other matrix together
        added_row=[]
        added_matrix=[]
        if self.matrix1dim!=self.otherdim:
            print("The two matrices cannot be added since the dimensions are not equal")
            return None
        for i in range(self.matrix1dim[0]):
            for j in range(self.matrix1dim[1]):
                added_row.append(self.matrix1[i][j]+self.other[i][j])
            added_matrix.append(added_row)
            added_row=[]
        print("Added matrix", added_matrix)
        return added_matrix

    def sub( self):##subtracts matrix1 from other matrix
        subbed_row=[]
        subbed_matrix=[]
        if self.matrix1dim!=self.otherdim:
            print("The two matrices cannot be subtracted since the dimensions are not equal")
            return None
        for i in range(self.matrix1dim[0]):
            for j in range(self.matrix1dim[1]):
                subbed_row.append(self.matrix1[i][j]-self.other[i][j])
            subbed_matrix.append(subbed_row)
            subbed_row=[]
        print("Subbed matrix", subbed_matrix)
        return subbed_matrix

    def mult( self):##multiplies matrix1 by other matrix
        mult_row=[]
        mult_matrix=[]
        vector1=[]
        vector2=[]
        vector1_1=[]
        vector2_2=[]
        if self.otherdim[0]==1 and self.otherdim[1]==1:##calculations for scalar multiplication

            for i in range(self.matrix1dim[0]):
                for j in range(self.matrix1dim[1]):
                    mult_row.append(self.matrix1[i][j]*self.other[0][0])
                mult_matrix.append(mult_row)
                mult_row=[]
            print("scalar multiplied matrix", mult_matrix)
            return mult_matrix

        else:##calculates two matrices multiplication
            if self.matrix1dim[1]==self.otherdim[0]:
                for i in range(self.matrix1dim[0]):
                    for j in range(self.matrix1dim[1]):
                        vector1.append(self.matrix1[i][j])
                    vector1_1.append(vector1)
                    for a in range(self.otherdim[1]):
                        for s in range(self.otherdim[0]):
                            vector2.append(self.other[s][a])
                        vector2_2.append(vector2)
                        dotsum=self.dot(vector1_1,vector2_2)
                        vector2=[]
                        vector2_2=[]
                        mult_matrix.append(dotsum)
                    vector1_1=[]
                    vector1=[]

                counter=0
                mult1=[]
                mult2=[]

                for y in mult_matrix:##makes mult matrix divided by rows
                    counter+=1
                    if counter%self.otherdim[1]==0:
                        mult1.append(y)
                        mult2.append(mult1)
                        mult1=[]
                    if counter%self.otherdim[1]!=0:
                        mult1.append(y)





                print("This is your multiplied matrix",mult2)
                return mult2
            else:
                print("The two matrices cannot be multiplied")
                return None


    def dot(self,vector1,vector2):##returns a single dot sum for 2 vectors
        dotsum=0
        dotsumlist=[]
        counter=self.matrix1dim[0]
        for i in range(self.matrix1dim[1]):
            dotsumlist.append(vector1[0][i]*vector2[0][i])
        for j in dotsumlist:
            dotsum+=j
        return dotsum

    def transpose( self ):
        transpose_matrix_column=[]
        counter=0
        for i in range(self.matrix1dim[0]):
            for j in range(self.matrix1dim[1]):

                if i==0:
                    transpose_matrix_column.append([self.matrix1[i][j]])
                else:
                    transpose_matrix_column[j].append(self.matrix1[i][j])
                    counter+=1
        print("Transposed matrix",transpose_matrix_column)
        return transpose_matrix_column

def main():
    print("input example: if you wanted a 2x2 matrix containing 1,2,3,4 you would format it 1 2/3 4")
    MatrixA=input("Enter the numbers for matrix one, divide rows by using the '/' key")
    MatrixB=input("Enter the numbers for matrix two, divide rows by using the '/' key, or enter scalar number")
    try:
        Matrix1=listoflists(MatrixA)
        Matrix2=listoflists(MatrixB)
        M=Matrix(Matrix1,Matrix2)
    except:
        print("not a valid input")
        main()
    
    
main()
    
