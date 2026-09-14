class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result =[0]*len(nums)
        p_s = 0
        n_s = 1
        for num in nums:
            if num < 0 :
                result[n_s] = num
                n_s+=2
            else:
                result[p_s] = num
                p_s +=2
        return result
        