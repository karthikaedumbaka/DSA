class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 1
        if n==1 or n==0:
            return True
            
        for i in range(n*2):
            if nums[(i%n)] >= nums[(i-1)%n]:
                count +=1
            else:
                count = 1
            if count == n:
                return True
        return False

        # Time : O(n)
        #space O(1)