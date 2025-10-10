class Solution:
    def fib(self, n: int) -> int:
        if n <=1:
            return n
        return self.fib(n-1) + self.fib(n-2)
        # time 2^n
        #space 2^n