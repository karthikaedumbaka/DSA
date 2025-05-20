class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.nums=nums
        self.target =target
        for i in range (0,len(nums)):
            if nums[i]==target:
                return i
        return -1
        