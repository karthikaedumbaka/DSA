class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return self.power(n)

    def power(self,n):
        if n<=0:
            return False
        if 1162261467 % n==0:
            return True
        else:
            return False

        return self.power(n//3)
        