class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #Bf 
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2 
        nums=sorted(nums)
        return nums
        # time NlogN(for sorting) . N to for loop (O(N))
        # space O(1)
        
        