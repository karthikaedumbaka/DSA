class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        prf = 1
        suf = 1
        max_produxt = float('-inf')
        for i in range(n):
            if prf == 0:
                prf = 1
            if suf == 0:
                suf = 1
            prf *= nums[i]
            suf *=nums[n-i-1]
            max_produxt = max(max_produxt,prf,suf)
        return max_produxt



            
