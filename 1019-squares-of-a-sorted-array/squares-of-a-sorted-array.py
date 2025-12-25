class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # #Bf 
        # for i in range(len(nums)):
        #     nums[i] = nums[i] ** 2 
        # nums=sorted(nums)
        # return nums
        # # time NlogN(for sorting) . N to for loop (O(NlogN))
        # # space O(1)
        

        # best 
        # for i in range(len(nums)):
        #     nums[i] = nums[i] ** 2
        # #[16,1,0,9,100]
        # # print(nums)
        # l = 0
        # r = len(nums)-1
        # ans = []
        # while  l <= r :
        #     if nums[l] < nums[r]:
        #         ans.append(nums[r])
        #         r-=1
        #     else : 
        #         ans.append(nums[l])
        #         l+=1
        # # swaping
        # a=0
        # b=len(ans)-1
        # while a<b:
        #     ans[a] ,ans[b] = ans[b] ,ans[a]
        #     a+=1
        #     b-=1
        # return ans

        # the best  
        # [-4,-1,0,3,10]
        ans = [0] * len(nums)
        l = 0
        r = len(nums)-1
        write = len(nums) -1
        while l <= r :
            left = nums[l] ** 2 
            right =nums[r] ** 2 
            if left  < right :
                ans[write] = right
                r-=1
            else:
                ans[write] = left
                l+=1
            write -=1
        return ans



        