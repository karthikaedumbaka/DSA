class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 :
            return [-1,-1]
        min_num = -1
        max_num = -1
        L = 0 
        R = len(nums)-1
        while L <=R:
            mid = (L+R)//2
            if nums[mid] == target:
                min_num = mid
                R-=1
            elif nums[mid] <target:
                L+=1
            else:
                R -=1
        L = 0 
        R = len(nums)-1                
        while L <=R:
            mid = (L+R)//2
            if nums[mid] == target:
                max_num = mid
                L+=1
            elif nums[mid] <target:
                L+=1
            else:
                R -=1
        return [min_num,max_num]