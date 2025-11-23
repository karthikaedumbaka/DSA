class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=1 # check for length of unique number lenght
        for j in range(1,len(nums)):
            if nums[j] != nums[j-1]:   # checking for defense
                nums[i] = nums[j]
                i+=1
        return i  
        # time O(n)
        # space O(1)