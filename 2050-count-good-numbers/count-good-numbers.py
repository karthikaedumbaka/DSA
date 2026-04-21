import math
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = (10**9) + 7
        def helper(base , exp ,mod) :
            if exp == 0 :
                return 1
            res = helper(base , exp//2 ,mod)
            res = (res * res) % mod
            if exp %2:
                res = (res * base) % mod
            return res
        even_place = (n+1) //2
        odd_place = n//2
        return (helper(5,even_place,MOD) * helper(4,odd_place,MOD)) % MOD
        

        