class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        r=len(matrix)
        c=len(matrix[0])

        for i in range(1,r):
            for j in range(c):

                if j==0:
                    matrix[i][j]=matrix[i][j]+min(matrix[i-1][j], matrix[i-1][j+1])
                if j==c-1:
                    matrix[i][j]=matrix[i][j]+min(matrix[i-1][j], matrix[i-1][j-1])
                if 0<j<c-1:
                    matrix[i][j]=matrix[i][j]+min(matrix[i-1][j], matrix[i-1][j-1], matrix[i-1][j+1])
        
        return min(matrix[r-1])
        