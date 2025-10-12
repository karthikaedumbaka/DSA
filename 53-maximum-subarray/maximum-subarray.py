class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = float('-inf')
        currSum = 0 
        for n in nums:
            if currSum < 0 :
                currSum =0
            currSum +=n
            maxi = max(maxi , currSum)
        return maxi