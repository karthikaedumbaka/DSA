class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        palindromeNumber = 0 
        real_number = x
        while x >0:
            palindromeNumber *=10
            palindromeNumber += x%10
            x=x//10
        return True if palindromeNumber==real_number  else False