class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = float("inf")
        left = 0
        summ = 0
        for right in range(len(nums)):
            summ+=nums[right]
            while summ >= target:
                result = min (result , right - left +1)
                summ -= nums[left]
                left +=1
        if result == float("inf"):
            return 0
        return result
# c=Solution()
# c.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3])
            
        