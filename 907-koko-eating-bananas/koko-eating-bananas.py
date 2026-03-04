import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 
        r = max(piles) # o(n)
        result = r
        while l<=r:
            k = (l+r)//2
            hrs = 0 
            for pile in piles:
                hrs += math.ceil(pile/k)
            if hrs <= h:
                result= min(k,result)
                r = k-1
            else:
                l =k+1

        return result
# Time  : O(n log m)
# Space : O(1)