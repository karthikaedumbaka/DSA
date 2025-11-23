class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i =0 
        while i <len(nums):
            if nums[i] == 0:
                break
            i+=1
        if i == len(nums):
            return nums
        j=i+1
        while j< len(nums):
            if nums[j] !=0:
                nums[j] ,nums[i] = nums[i] ,nums[j]
                i+=1
            j+=1
        return nums