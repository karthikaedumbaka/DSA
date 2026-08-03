class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # L  = len(nums)
        # if L == 0 or L == 1 :
        #     return nums
        
        # E = 0 
        # for i in range(L-1,-1,-1):
        #     if nums[i] != 0:
        #         E=i
        #         break
        # S = 0 
        # for j in range(L):
        #     if nums[j] == 0 :
        #         S = j
        #         break
        # while S<= E:
        #     if  nums[S] ==0 :
        #         nums[E] ,nums[S] = nums[S],nums[E]
        #         E-=1
        #     S+=1
        # return nums
        n = len(nums)
        zero_index = -1
        for i in range(n):
            if nums[i] ==0 :
                zero_index = i 
                break
        if zero_index == -1 : return nums

        for p in range(zero_index+1,n):
            if nums[p] != 0 :
                nums[p] , nums[zero_index] = nums[zero_index] , nums[p]
                zero_index +=1
        return nums


            
        

        