class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dp = deque()  # stores indices
        result = []
        l=r=0

        while r < len(nums):
            while dp  and nums[dp[-1]] < nums[r] :
                dp.pop()
            dp.append(r)

            if l > dp[0] :
                dp.popleft()
            if (r+1) >= k:
                result.append(nums[dp[0]])
                l+=1
            r+=1
        return result


