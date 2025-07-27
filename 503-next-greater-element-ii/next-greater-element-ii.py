class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums) # to get the lenght of arr
        stk=[] # for stacks 
        ans=[-1]* n 

        for i in range (2*n -1,-1, -1):
            while stk and stk[-1] <= nums[i%n] :
                stk.pop()
            if i<n:
                if stk:
                    ans[i] = stk[-1]
            stk.append(nums[i%n])
        return ans

        #time 0(n)
        
        