class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix) #row
        m = len(matrix[0]) #col

        row = 0
        col = m -1 #15
        while row <n and col >=0:
            if matrix[row][col] ==target:
                return True
            elif matrix[row][col] >target:
                col -=1
            else:
                row +=1 
        return False
            

        