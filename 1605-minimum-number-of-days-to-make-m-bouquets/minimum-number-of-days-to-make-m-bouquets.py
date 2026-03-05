class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay)  < m*k:
            return -1
        l = min(bloomDay) # o(n)
        r = max(bloomDay) # O(n)
        ans = -1
        while l<=r:
            mid = (l+r) //2
            if self.is_possible(bloomDay,mid,m,k):
                ans = mid
                r = mid -1
            else:
                l = mid+1
        
        return ans

    def is_possible(self,bloomDay,mid,m,k):
        count = 0 
        possible_count = 0
        for b in bloomDay:
            if b <=mid:
                count+=1
                if count == k:
                    possible_count +=1
                    count =0
            else:
                count =0
        
        return possible_count >=m
                


        