class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:\
    # BF
    #time O(N*K)
    # space O(1)
        # max_avg = float("-inf")
        # n=len(nums)
        # if len(nums) == 1 :
        #     return nums[0]

        # for i in range(n-k+1):
        #     k_size = 0
        #     for j in range(i,i+k):
        #         k_size += nums[j]
        #     k_avg = k_size/k
        #     max_avg = max(max_avg,k_avg)
        
        # return max_avg

        ans = float("-inf")
        n=len(nums)
        first_k=0
        for i in range(k):
            first_k += nums[i]
        k_avg = first_k / k 
        ans = max(ans,k_avg )

        for i in range(k,n):
            first_k += nums[i]
            first_k -= nums[i-k]
            k_avg = first_k / k
            ans = max(ans,k_avg )
        return ans


    
