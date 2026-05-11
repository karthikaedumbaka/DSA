class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        summ = nums[0]
        for i in range(1,len(nums)):
            nums[i] += summ
            summ = nums[i]
        return nums

    # time O(n)
    # space O(1)
        