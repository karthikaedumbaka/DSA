class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # l=1
        # for i in range(len(nums)):
        #     if nums[i] != nums[l-1]:
        #         nums[l] = nums[i]
        #         l+=1

        # return l
        #time O(n)
        # space O(1)

        i=1
        for j in range(len(nums)):
            if nums[j] != nums[i-1]:
                nums[i] = nums[j]
                i+=1
        return i
                
            
            
        