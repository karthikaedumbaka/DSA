class Solution:
    def reverse(self, x: int) -> int:
        
        result =0
        Find_pos = 1 if x>0 else 0
        x = abs(x)
        while x > 0:
            result = result *10
            result += x%10
            x = x//10
        if (result < (-(2**31))) or (result > ((2**31)-1)):
            return 0
        return result if Find_pos else -result
# time O(N)
#space O(1)