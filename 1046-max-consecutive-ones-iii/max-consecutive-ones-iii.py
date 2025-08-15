class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # n=len(nums)
        # ans=0
        # for i in range(n):
        #     for j in range(i,n):
        #         temp=k
        #         is_valid=True
        #         for z in range(i,j+1):
        #             if nums[z] ==0:
        #                 if temp>0:
        #                     temp-=1
        #                 else:
        #                     is_valid=False
        #                     break
        #         if is_valid:
        #             ans=max(ans,j-i+1)
        # return ans
        max_length = 0  # Maximum subarray length
        left = 0        # Left boundary of sliding window
        right = 0       # Right boundary of sliding window
        zeros = 0       # Count of zeros in current window
        n = len(nums)
        
        while right < n:
            # Expand window to the right
            if nums[right] == 0:
                zeros += 1
                
            # Contract window from the left if too many zeros
            if zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
                
            # Update maximum length
            if zeros <= k:
                length = right - left + 1
                max_length = max(max_length, length)
                
            # Continue expanding the window
            right += 1
            
        return max_length
