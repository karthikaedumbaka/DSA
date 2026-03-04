class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return nums[0]
        if nums[0] != nums[1] :
            return nums[0] 
        if nums[-1] != nums[-2]:
            return nums[-1] 

        l = 1
        r = len(nums)-2
        while l <=r :
            mid = (l+r) //2 
            
            if (nums[mid-1] != nums[mid]  and  nums[mid] != nums[mid+1]):
                return nums[mid]
            leftSide = mid - 1  if nums[mid-1] == nums[mid]  else mid
            if leftSide % 2:
                r = mid -1
            else:
                l =mid +1

        # time O(log n)
        #space (O(n))

