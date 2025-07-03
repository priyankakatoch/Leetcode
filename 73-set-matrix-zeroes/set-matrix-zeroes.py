class Solution:
    def setZeroes(self, matrix):
        row = len(matrix)
        clo = len(matrix[0])
        def set_matrix(matrix,r,c):
            for i in range(0,row):
                if matrix[i][c] != 0:
                    matrix[i][c]=float("inf")
            for j in range(0,clo):
                if matrix[r][j]!=0:
                    matrix[r][j]=float("inf")
        for i in range (0,row):
            for j in range (0,clo):
                if matrix[i][j]==0:
                    set_matrix(matrix,i,j)
        
        for i in range(0,row):
            for j in range(0,clo):
                if matrix[i][j]==float("inf"):
                    matrix[i][j] = 0        