class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        l = 0 
        r =len(height)-1
        while l < r:
            max_water = max(max_water,min(height[l],height[r]) * (r -l))
            if l < r and height[l] < height[r]:
                l+=1
            else:
                r-=1
        return max_water

       