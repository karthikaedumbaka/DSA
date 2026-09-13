class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_len = 0 
        i = 0 
        for j in range(len(nums)):
            if nums[j] ==1:
                max_len = max(max_len, j-i+1)
            else:
                i=j+1
        return max_len


        