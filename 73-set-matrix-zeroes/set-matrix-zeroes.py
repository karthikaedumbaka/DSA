class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])
        img_row = [1] * len(matrix)
        img_col = [1] * (len(matrix[0]))
        for i in range(row) : 
            for j in range(col) :
                if matrix[i][j] == 0 :
                    img_row[i] = -1
                    img_col[j] = -1
        
        for i in range(row):
            for j in range(col):
                if img_row[i]== -1 or img_col[j] ==-1:
                    matrix[i][j] =0
        
         

        
        