# Python3 program to change value of
# diagonal elements of a matrix to 0.
 
# method to replace the diagonal
# matrix with zeros
def diagonalMat(row, col, m):
 
    # l is the left iterator which is
    # iterationg from 0 to col-1[4] here
    # k is the right iterator which is
    # iterating from col-1 to 0
    i, l, k = 0, 0, col - 1;
 
    # i used to iterate over rows of the matrix
    while(i < row):
        j = 0;
         
        # condition to check if it is
        # the centre of the matrix
        if(l == k):
            m[l][k] = 0;
            l += 1;
            k -= 1;
             
        # otherwize the diagonal will be equivalaent to l or k
        # increment l because l is traversing from left
        # to right and decrement k for vice-cersa
        else:
            m[i][l] = 0;
            l += 1;
            m[i][k] = 0;
            k -= 1;
             
        # print every element
        # after replacing from the column
        while(j < col):
            print(" ", m[i][j], end = "");
            j += 1;
        i += 1;
        print("");
 
# Driver Code
if __name__ == '__main__':
    m = [[2, 1, 7 ],
        [ 3, 7, 2 ],
        [ 5, 4, 9 ]];
    row, col = 3, 3;
    diagonalMat(row, col, m);