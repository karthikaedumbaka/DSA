class Solution:
    def maxArea(self, height: List[int]) -> int:

        i,j =0,len(height)-1
        ans = 0 
        while i < j :
            if  height[i] ==0:
                i+=1
            elif height[j] ==0:
                j-=1
            width =j-i
            a=min(height[i],height[j])
            ans=max(ans,width*a)
            if height[i] < height[j] :
                i+=1
            else :
                j-=1
        return ans


