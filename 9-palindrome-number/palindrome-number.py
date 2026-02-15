class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp_x =x 
        if x < 0:
            return False
        revNum = 0
        while x > 0:
            lastNum = x % 10
            revNum = revNum *10 + lastNum
            x = x //10 

        return True if revNum == temp_x  else False 
        