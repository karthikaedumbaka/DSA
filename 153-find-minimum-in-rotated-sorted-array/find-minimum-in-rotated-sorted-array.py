class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) -1
        min_val = float("inf")
        while l <=r :
            mid = (l+r) //2
            if nums[l] <= nums[mid]:
                min_val = min(min_val,nums[l])
                l = mid+1
            else:
                min_val = min(min_val,nums[mid])
                r=mid-1
        return min_val