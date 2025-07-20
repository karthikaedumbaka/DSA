class Solution:
    def maxArea(self, height: List[int]) -> int:
        # bf
        i,j =0,len(height)-1
        ans = 0 
        while i < j :
            width =j-i
            a=min(height[i],height[j])
            ans=max(ans,width*a)
            if height[i] < height[j] :
                i+=1
            else :
                j-=1
        return ans


