class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0 
        while n!=0:
            n = n & (n-1)
            ans+=1
        return ans 
        #time  O(1)
        #space O(n)

        