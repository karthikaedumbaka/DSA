class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l =  max(weights) 
        r = sum(weights)
        
        while l<=r:
            mid = (l+r)//2 
            needed = self.daysNeed(weights,mid)
            if needed<= days:
                r = mid -1
            else:
                l = mid + 1
        return l

                
    def daysNeed(self,weights,mid):
        days =1 
        currentLoad = 0
        for weight in weights:
            if currentLoad + weight > mid:
                days+=1
                currentLoad =weight
            else:
                currentLoad +=weight
        return days


