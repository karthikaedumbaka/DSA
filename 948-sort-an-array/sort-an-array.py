class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # insention Sort
        # n=len(nums)
        # for i in range(1,n):
        #     j=i-1
        #     while j>=0 and nums[j]  > nums[j+1]:
        #         nums[j] ,nums[j+1] = nums[j+1] , nums[j]
        #         j-=1
        # return nums
        # # mearge sort
        if len(nums) <= 1:
            return nums
        mid = len(nums)//2
        left_arr = nums[:mid]
        right_arr = nums[mid:]
        left=self.sortArray(left_arr)
        right=self.sortArray(right_arr)
        return self.merge_arr(left,right)
    def merge_arr(self,left,right):
        result = []
        i,j=0,0
        n,m=len(left),len(right)
        while i < n and j < m:
            if left[i] <= right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        while i<n:
            result.append(left[i])
            i+=1
        while j<m:
            result.append(right[j])
            j+=1
        return result

