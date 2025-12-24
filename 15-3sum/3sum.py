class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #BF
        # make 3 loops inside 
        # ans=set()
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             if  (nums[i] + nums[j] + nums[k] ==0) :
        #                 ans.add(tuple(sorted([nums[i], nums[j], nums[k]])))



                        
        # return [ i for i in ans ]
        ans = set()
        nums= sorted(nums)
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    ans.add(tuple(sorted([nums[i] , nums[j] , nums[k]])))
                    j+=1
                    k-=1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -=1
                else:
                    j+=1
        return [list(x) for x in ans]






        