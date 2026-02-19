class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # BF
        # # (m,n) m = row , n = cols
        # row = len(matrix)
        # col = len(matrix[0])

        # for r in range(row):
        #     for c in range(col):
        #         if matrix[r][c] ==0:
        #             for m in range(col): #m row 
        #                 if matrix[r][m] !=0:
        #                     matrix[r][m] = "a"
        #             for n in range(row):
        #                 if matrix[n][c] !=0:
        #                     matrix[n][c] = "a"
        #             matrix[r][c] = "a"
        
        # for r in range(row):
        #     for c in range(col):
        #         if matrix[r][c] == "a":
        #             matrix[r][c] = 0
        
        # return matrix
        # better slo
        col = len(matrix[0])
        row = len(matrix)
        col_m = [0]* col
        row_m = [0]* row
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    row_m[r] = 1
                    col_m[c] = 1
        for r in range(row):
            for c in range(col):
                if (row_m[r] ==1 or col_m[c] ==1 ):
                    matrix[r][c] = 0
        
        return matrix


                           
                    

