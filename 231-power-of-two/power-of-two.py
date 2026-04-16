class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return self.power(n)

    def power(self,n):
        if n == 1:
            return True
        if n<=0 or n%2 !=0:
            return False
        return self.power(n // 2)
        

        