class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # BF
        # max_arae = 0
        # l = len(heights)
        # for i in range(l):
        #     height = heights[i]
        #     left ,right = i-1 ,i+1
        #     while left >=0 and heights[left] >= heights[i]:
        #         left -=1
        #     while right < l and heights[right] >= heights[i]:
        #         right +=1
        #     width = right - left -1
        #     max_arae =max(max_arae ,height * width )
        # return max_arae
        '''
        if you see the pattern we can see 
        left is prev_smaller
        right is next_smaller

        '''
        ans = 0 
        l= len(heights)
        left = self.left_height(heights)
        right = self.right_height(heights)
        for i in range(l):
            width = right[i] - left[i]  -1
            ans =max(ans ,width *heights[i] )
        return ans

    def left_height(self,heights):
        l = len(heights)
        result = [-1]* l
        # why -1 see if we donot have the any small 
        stk = [ ]
        for i in range(l) :
            while stk  and heights[stk[-1]] >= heights[i]:
                stk.pop()
            if stk:
                result[i] = stk[-1]
            stk.append(i)
        return result
    
    def right_height(self,heights):
        l = len(heights)
        result = [l]* l
        stk = [ ]
        for i in range(l):
            while stk and heights[stk[-1]] > heights[i]:
                idx = stk.pop()
                result[idx] = i
            stk.append(i)
        return result
    

        
            

        

