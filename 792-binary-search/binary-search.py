class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # l = 0 
        # r = len(nums) - 1
        # while l <= r:
        #     mid = (r+l) //2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] < target:
        #         l = mid+1
        #     else:
        #         r = mid -1
        
        # return -1
        return self.binary_search(nums,target,0,len(nums)-1)
    def binary_search(self,nums:List[int],target:int,l:int ,r:int) -> int:
        if l>r:
            return -1
        mid = (l+r)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binary_search(nums,target,mid+1,r)
        else:
            return self.binary_search(nums,target,l,mid-1)

            
        
        
        


        