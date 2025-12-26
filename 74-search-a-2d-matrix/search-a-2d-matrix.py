class Solution:
    def searchMatrix(self, matrix, target):
        row = -1
        t = 0
        b = len(matrix) -1
        while t <=b :
            mid = (t+b) //2 
            if matrix[mid][0] <=  target  <= matrix[mid][-1]:
                row = mid
                break
            elif  matrix[mid][0] >  target:
                b = mid -1
            else :
                t =mid +1
        if row == -1:
            return False
        l = 0 
        r = len(matrix[row])-1
        while l <=r :
            mid = (l+r)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] >target:
                r = mid -1
            else:
                l = mid +1
        return False