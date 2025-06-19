class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row=-1
        i,j=0,len(matrix)-1
        while i<=j:
            mid=(i+j)//2
            if matrix[mid][0] > target:
                row=mid-1
                j=mid-1
            else:
                i=mid+1

        l,r=0,len(matrix[row])-1
        while l<=r:
            mid=(l+r)//2
            if matrix[row][mid]==target:
                return True
            elif matrix[row][mid]>target:
                r=mid-1
            else:
                l=mid+1
        return False 
            



        