class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output=[0]*(n *2)
        for i in range(0,len(nums)):
            output[i] = nums[i]
            output[i+n]=nums[i]
        return output

        