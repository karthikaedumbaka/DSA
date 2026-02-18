class Solution:
    def findMaxConsecutiveOnes(self, nums):
        maxConsecutiveOnes = 0

        i =0
        for j in range(len(nums)):
            if nums[j] == 1:
                maxConsecutiveOnes =max(maxConsecutiveOnes,j-i+1)
            else:
                i= j+1
        
        return maxConsecutiveOnes