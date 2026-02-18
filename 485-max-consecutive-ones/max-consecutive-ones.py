class Solution:
    def findMaxConsecutiveOnes(self, nums):
        # maxConsecutiveOnes = 0

        # i =0
        # for j in range(len(nums)):
        #     if nums[j] == 1:
        #         maxConsecutiveOnes =max(maxConsecutiveOnes,j-i+1)
        #     else:
        #         i= j+1
        
        # return maxConsecutiveOnes

        maxConsecutiveOnes = 0
        current_count = 0
        for num in nums:
            if num == 1:
                current_count +=1
                maxConsecutiveOnes = max(maxConsecutiveOnes,current_count)
            else:
                current_count =0
        return maxConsecutiveOnes
