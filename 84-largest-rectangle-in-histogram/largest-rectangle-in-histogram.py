class Solution:
    def next_smaller(self,arr: List[int]) -> List[int]:
        stk = []
        n=len(arr)
        ans = [n for i in arr]
        for i in range(n-1,-1,-1):
            while len(stk) >0 and arr[stk[-1]] >= arr[i]:
                stk.pop()
            if len(stk) >0:
                ans[i] = stk[-1]
            stk.append(i)
        return ans
    def prev_smaller(self,arr: List[int]) -> List[int]:
        stk = []
        n=len(arr)
        ans = [-1 for i in range(n)]
        for i in range(n):
            while len(stk) >0 and arr[stk[-1]] >= arr[i]:
                stk.pop()
            if len(stk) >0:
                ans[i] = stk[-1]
            stk.append(i)
        return ans



    def largestRectangleArea(self, heights: List[int]) -> int:
        '''# your rectangle can cover area from mulitple bar
        # For BruteForce , we can check with all the possible rectangle -- ? 
        # rectangle  has 2 thigs , height , width
        # traverse over the array , for each i asume that to be the height of rectangle 
        ans=0
        for i in range(len(heights)):
            height= heights[i]
            left = i-1
            right = i+1
            while left >=0 and heights[left] >= height:
                left -=1
            while right <len(heights) and heights[right] >= height:
                right +=1
            width = right - left - 1
            ans=max(ans,height * width)
        return ans
        # time O(n^2)
        # space O(1)'''
        ans =0
        next_smaller = self.next_smaller(heights)
        prev_smaller = self.prev_smaller(heights)
        for i in range(len(heights)):
            height = heights[i]
            width = next_smaller[i] -prev_smaller[i] -1
            ans = max(ans,height*width) 
        return ans
        



    
        