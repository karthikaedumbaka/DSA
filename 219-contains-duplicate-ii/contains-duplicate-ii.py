class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l=0
        window = set()
        for r in range(l,len(nums)):
            if abs(l-r) > k :
                window.remove(nums[l])
                l+=1
        
            
            if nums[r] in window:
                return True
            window.add(nums[r])
        return False