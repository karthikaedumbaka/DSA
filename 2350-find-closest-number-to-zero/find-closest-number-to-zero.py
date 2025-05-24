class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=nums[0]
        if not nums:
            return None

        for i in nums[1:]:
            if abs(i)<abs(a):
                a=i
            elif abs(i)== abs(a) and i>a:
                a=i
        return a

        