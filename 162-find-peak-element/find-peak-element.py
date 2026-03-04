class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) ==1 :
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-2] < nums[-1]:
            return len(nums)-1
        l = 1
        r = len(nums)-2
        while l<=r :
            mid = (l+r)//2
            if (nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]):
                return mid
            elif nums[mid-1] < nums[mid] < nums[mid+1] :
                l=mid+1
            else:
                r=mid -1
        return -1
        # time O(log n)
        # space O(1)

        # Note:
# If the question asks for the greatest element in a general array,
# the time complexity becomes O(N) because we must scan all elements.
# But if the array is a mountain array, we can still use binary search
# to find the maximum in O(log n