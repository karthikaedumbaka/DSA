class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''# BF
        for i in range(0,len(nums)): ##### O(n) itis check every values in list
            for j in range(i+1,len(nums)): ##### O(n) itis check every values in list after i 
                if nums[i]+nums[j]==target: # o(1)
                    return [i,j]
         # time O(n2)
         # space O(1)'''
        #  target  = nums[i]+nums[j]
        #  nums[i]=target-nums[j]
        #  remaining  = target - values

        d= dict()
        for index,value in enumerate(nums):
            remaining = target - value
            if remaining in d:
                return([ d[remaining],index ])
            else:
                d[value] = index
        return [-1,-1]