class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = set()
        for i in range(0,len(nums)):
            j=i+1
            k = len(nums) -1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    ans.add(tuple([nums[i] , nums[j] , nums[k]]))
                    j+=1
                    k-=1
                elif nums[i] + nums[j] + nums[k] < 0:

                    j+=1
                else:
                    k-=1
        return [list(x) for x in ans]

        