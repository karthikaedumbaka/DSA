class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = -1
        for idx in range(len(nums)-2 ,-1,-1 ):
            if nums[idx] < nums[idx+1]:
                index = idx
                break
        if index == -1:
            nums.reverse()
            return
        for idx in range(len(nums)-1,index,-1):
            if nums[idx] > nums[index]:
                nums[idx],nums[index] = nums[index] ,nums[idx]
                break
        nums[index+1:] = reversed(nums[index+1:])
            
        
