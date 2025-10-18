from math import isqrt

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        prime  = [True] * n
        prime[0] = prime[1] =False

        for p in range(2,isqrt(n)+1):
            if prime[p]:
                for m in range(p*p , n ,p ):
                    prime[m] =False
        return sum(prime)

        