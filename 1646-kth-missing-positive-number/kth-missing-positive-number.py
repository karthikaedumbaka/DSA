class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_value = 0
        i = 1
        while k !=0 :
            if i not in arr:
                missing_value = i
                k-=1
            i+=1
        
        return missing_value
