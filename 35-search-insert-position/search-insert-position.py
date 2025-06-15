class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i=0
        j=len(nums)-1
        
        while i<=j:
            mid=(i+j)//2
            if target == nums[mid]:
                return mid
            if nums[mid]<target:
                i=mid+1
            else:
                j=mid-1
        return i
            
        # time O(log n) 
        # space O(1)