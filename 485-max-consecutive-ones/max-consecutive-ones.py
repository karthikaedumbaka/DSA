class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0 
        curr = 0
        for i in nums:
            if i == 1:
                curr +=1
                count = max (count,curr)
            else:
                curr = 0
        return count

        