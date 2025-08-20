
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        d={}
        l=0
        f=0
        for r in range( len(nums)):
            d[nums[r]] = d.get(nums[r],0)+1
            while d[nums[r]] > k:
                d[nums[l]] -=1
                l+=1
            f=max(f,r-l+1)
        return f
# time O(N)
# space O(N)



        