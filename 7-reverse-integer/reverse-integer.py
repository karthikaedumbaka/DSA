class Solution:
    def reverse(self, x: int) -> int:
        
        revNum = 0 
        neg_num =   x > 0 
        x = abs(x)
        while x > 0 :
            lastNum = x % 10
            revNum = revNum * 10 + lastNum
            x = x // 10
        if revNum >  2**31 - 1:
            return 0
        return revNum if neg_num else  -revNum