# You are given a 2D array of integers. Print out the clockwise spiral traversal of the matrix.

# Example:

# grid = [[1,  2,  3,  4,  5],
#         [6,  7,  8,  9,  10],
#         [11, 12, 13, 14, 15],
#         [16, 17, 18, 19, 20]]

# The clockwise spiral traversal of this array is:

# 1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12

# Here is a starting point:





def matrix_spiral_print(M):
    
    k = 0
    for i in range(len(M)):
        j = k
        if( i % 2 == 0):
            for j in range(len(M)):
                print(M[i][j], end = " ")
        else :
            for l in range(len(M)):
                print(M[l][j], end = " ")
        k = j
            
grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]]

matrix_spiral_print(grid)
# 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12
