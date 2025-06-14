class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output=[0]*(n *2)
        for i,values in enumerate(nums):
            output[i] = values
            output[i+n]=values
        return output

        # big O(n)
        # space O(n)

        