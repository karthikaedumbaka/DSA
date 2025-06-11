class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        m= (n*(n +1))//2
        list_sum =sum(nums)
        return m-list_sum
        