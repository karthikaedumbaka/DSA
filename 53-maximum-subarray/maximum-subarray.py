class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        cur_sum = 0

        for idx in range(len(nums)):
            cur_sum+=nums[idx]

            if cur_sum > max_sum:
                max_sum = cur_sum

            if cur_sum <= 0:
                cur_sum = 0
        
        return max_sum

