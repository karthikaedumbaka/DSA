import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        ans = max(nums)
        l = 1
        r = max(nums)
        while l<=r:
            mid = (l+r)//2 
            all_sum = 0
            for num in nums:
                all_sum += math.ceil(num/mid)
            if all_sum <=threshold :
                ans = mid
                r =mid -1
            else:
                l = mid +1
        return ans  

