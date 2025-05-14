'''
Edge Cases:
[1,2,3,4] = [4,3,2,1] : Not an edge case
Assumptions: Proper N * N Matrix.
'''
matrix = [[1,2,3,4], [5,6,7,8],[9,10,11,12],[13,14,15,16]]
sezs = len(matrix)
print(" Size ", sezs)

def rotate_by_90_degrees_with_new_matrix(matrix):
    new_matrix = [[0 for i in range(len(matrix))] for list in range(len(matrix))]
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            new_matrix[i][j] = matrix[j][size-1-i]
    return new_matrix

def rotate_by_90_degree_in_place(matrix):
    length = len(matrix) - 1
    num_layers = len(matrix)//2
    for i in range(num_layers):
        for j in range(i,length - i):
            top_left = matrix[i][j]
            matrix[i][j] = matrix[j][length-i]
            matrix[j][length-i] = matrix[length-i][length-j]
            matrix[length-i][length-j] = matrix[length-j][i]
            matrix[length-j][i] = top_left
           

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], " ", end = " ")
        print()


rotate_by_90_degree_in_place(matrix)
print_matrix(matrix)
