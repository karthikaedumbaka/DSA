class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r=0,len(nums)-1
        while l<=r:
            m=(l+r)//2
            if nums[m] == target:
                return m
            elif nums[l]<=nums[m]:
                if nums[l] <= target and target <= nums[m]:
                    r=m-1
                else:
                    l=m+1
            else:
                if nums[m] <= target and target <= nums[r]:
                    l=m+1
                else:
                    r=m-1
        return -1